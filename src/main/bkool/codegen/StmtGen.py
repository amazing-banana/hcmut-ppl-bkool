from functools import reduce
from typing import (
    TYPE_CHECKING,
    Any,
    Generator,
    Iterable,
    List,
    Sequence,
    Tuple,
    Optional,
    Union,
)

from AST import *
from AdditionalTypes import *
from CodeGenSymbol import (
    Exprs,
    FuncDef,
    TypeDef,
    LocalVar,
    LocalConst,
    Access,
    VarDefGeneric,
)
from Emitter import Emitter  # type: ignore
from ExprEval import ExprEval
from ExprGen import ExprGen
from Frame import Frame
from Visitor import BaseVisitor

if TYPE_CHECKING:
    from CodeGenSymbol import GlobalClassTable, LocalDefType

__all__ = ["StmtGen"]

str_t = StringType()
int_t = IntType()
float_t = FloatType()
bool_t = BoolType()
void_t = VoidType()
null_t = NullType()


def filter_members(decls: "List[Union[AttributeDecl,MethodDecl,Any]]"):
    attrs: "List[AttributeDecl]" = []
    stat_inits: "List[StoreDecl]" = []
    inst_inits: "List[StoreDecl]" = []
    methods: "List[MethodDecl]" = []
    ctors: "Optional[MethodDecl]" = None
    for decl in decls:
        if isinstance(decl, MethodDecl):
            if decl.name.name == "<init>":
                ctors = decl
            else:
                methods.append(decl)
        else:
            attrs.append(decl)
            inner_decl = decl.decl
            if isinstance(decl.kind, Static):
                if isinstance(inner_decl, VarDecl):
                    if inner_decl.varInit is not None:
                        stat_inits.append(inner_decl)
                else:
                    if inner_decl.constant is not None:
                        stat_inits.append(inner_decl)
            else:
                if isinstance(inner_decl, VarDecl):
                    if inner_decl.varInit is not None:
                        inst_inits.append(inner_decl)
                else:
                    if inner_decl.constant is not None:
                        stat_inits.append(inner_decl)
    return attrs, methods, stat_inits, inst_inits, ctors


def attr_inits(attrs, base):
    # type: (Sequence[Any], Union[SelfLiteral, Id]) -> Generator[Assign, None, None]
    for a in attrs:
        if isinstance(a, VarDecl):
            assert a.varInit
            yield Assign(FieldAccess(base, a.variable), a.varInit)
        else:
            assert a.value
            yield Assign(FieldAccess(base, a.constant), a.value)


def local_inits(stores, prev, post):
    # type: (List[StoreDecl], List[Access], List[Access]) -> Generator[Tuple[Assign,Access,Access], None, None]
    for v, a, b in zip(stores, prev, post):
        if isinstance(v, VarDecl) and v.varInit:
            yield Assign(v.variable, v.varInit), a, b
        elif isinstance(v, ConstDecl) and v.value:
            yield Assign(v.constant, v.value), a, b


class CtorObjects:
    def __init__(
        self,
        m: "MethodDecl",
        base: Union[SelfLiteral, Id],
        pname: "str",
        attrs: "List[StoreDecl]",
        pctor_no_args: "Optional[bool]",
    ) -> None:
        self.ast = m
        self.base = base
        self.pname = pname
        self.attrs = attrs
        self.pctor_no_args = pctor_no_args

    ...


def super_call(
    self: "StmtGen",
    ctor: "CtorObjects",
    mtype: "FuncType",
    frame: "Frame",
):
    """
    class A:                        | class A: ...
        A(a,b): ...                 | class B extends A:
    class B extends A:              |   B(a,b): ...
        var b = B(1,2);             |   var b = B(1,2);
    ->                              | ->
    A(a,b):                         | A():
     load this                      |  load this
     invokespecial Object:<init>()V |  invokespecial Object:<init>()V
    B(a,b) :                        | B(a,b):
     load this                      |  load this
     load a                         |  invokespecial A:<init>()V
     load b                         |
     invokespecial A:<init>(a,b)V   |
    """
    m = ctor.ast
    pname = ctor.pname
    pctor_no_args = ctor.pctor_no_args

    self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.current_CName)), 0, frame))

    if m.param and pname != "" and pctor_no_args is False:
        # If Ctor has args,
        # and Class has a Parent
        # and Parent has args ctor
        for i, e in enumerate(m.param):
            p = self.emit.emitREADVAR(e.variable.name, e.varType, i + 1, frame)
            self.emit.printout(p)

    if pname == "":  # If no Parent, call Object:<init>
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
    elif pctor_no_args is None or pctor_no_args:  # If Parent has Parent() ctor or no Ctor
        fname = f"{pname}/<init>"
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame, fname, FuncType([], VoidType())))
    else:  # Parent has Parent(a,...)
        fname = f"{pname}/<init>"
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame, fname, mtype))
    return


def genMethod(
    self: "StmtGen",
    m: "MethodDecl",
    ctor: "Optional[CtorObjects]",
    ac: "Access",
    frame: "Frame",
):
    c = ac.Clone(r=m.returnType)
    is_inst = isinstance(m.kind, Instance)
    mtype = FuncType([v.varType for v in m.param], m.returnType if m.returnType else void_t)
    self.emit.printout(self.emit.emitMETHOD(m.name.name, mtype, not is_inst, frame))

    frame.enterScope(True)

    start = frame.getStartLabel()
    end = frame.getEndLabel()

    if is_inst:
        new_index = frame.getNewIndex()
        this_type = ClassType(Id(self.current_CName))
        self.emit.printout(self.emit.emitVAR(new_index, "this", this_type, start, end, frame))

    for p in m.param:
        s: VarDefGeneric = self.visit(p, c)
        _i = frame.getNewIndex()
        s.local_index = _i
        var = self.emit.emitVAR(_i, p.variable.name, p.varType, start, end, frame)
        self.emit.printout(var)
        c = c.Clone(st=c.symtable.add(s))

    visit_block(self, m.body, ctor, mtype, c, frame)

    if isinstance(mtype.return_type, VoidType):
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
    elif ac.flow.is_reachable:
        raise Exception("Missing return statements somewhere!")

    ac.flow.method_exit()

    frame.exitScope()

    self.emit.printout(self.emit.emitENDMETHOD(frame))
    return


def visit_block(
    self: "StmtGen",
    b: "Block",
    ctor: "Optional[CtorObjects]",
    mtype: "Optional[FuncType]",
    ac: "Access",
    frame: "Frame",
):
    c = ac
    prev_assign_envs: "List[Access]" = []
    post_assign_envs: "List[Access]" = []
    start = frame.getStartLabel()
    end = frame.getEndLabel()

    for decl in b.decl:
        s = self.visit(decl, c)
        _i = frame.getNewIndex()
        s.local_index = _i
        self.emit.printout(self.emit.emitVAR(_i, s.name, s.type, start, end, frame))
        prev_assign_envs.append(c)
        c = c.Clone(st=c.symtable.add(s))
        post_assign_envs.append(c)

    self.emit.printout(self.emit.emitLABEL(start, frame))

    if ctor:
        if isinstance(ctor.base, SelfLiteral):
            assert mtype
            super_call(self, ctor, mtype, frame)

        for attr_init in attr_inits(ctor.attrs, ctor.base):
            self.visit(attr_init, ac)

    for local_init, prev, post in local_inits(b.decl, prev_assign_envs, post_assign_envs):
        visit_assign(self, local_init, prev, post)

    with ac.flow.enter_block(kind="func" if mtype else None):
        for stmt in b.stmt:
            self.emit.printout(self.emit.emitCOMMENT("_____________________"))
            self.visit(stmt, c)

    self.emit.printout(self.emit.emitLABEL(end, frame))
    return


def visit_assign(self, ast, prev_env, post_env):
    # type: (StmtGen, Assign, Access, Access) -> None
    """except for symtab, everything else in prev and post must be the same"""
    assert prev_env.frame is post_env.frame
    assert prev_env.emit is post_env.emit
    assert prev_env.sc is post_env.sc

    assert post_env.is_store is False

    rhs_ast = simpl_expr.visit(ast.exp, prev_env).ast

    lhs: "Exprs" = self.visit(ast.lhs, post_env)
    rhs: "Exprs" = expr_gen.visit(rhs_ast, prev_env)
    if isinstance(lhs.type, FloatType) and isinstance(rhs.type, IntType):
        right_code = rhs.codes + (self.emit.emitI2F(post_env.frame),)
    else:
        right_code = rhs.codes
    store_lhs: "Exprs" = self.visit(ast.lhs, post_env.Clone(sto=True))
    self.emit.buff.extend(lhs.codes + right_code + store_lhs.codes)
    return


def default_ctor(param_types: "Iterable[Type]"):
    return MethodDecl(
        Instance(),
        Id("<init>"),
        [VarDecl(Id(f"args{k}"), v, None) for k, v in enumerate(param_types)],
        VoidType(),
        Block([], []),
    )


def get_ctor(
    m: "Optional[MethodDecl]", pn: "Optional[Id]", ac: "GlobalClassTable"
) -> "Tuple[MethodDecl,Optional[bool]]":
    """
    class A:                    | class A: ...
        A(a,b): ...             | class B:
    class B extends A:          |   B(a,b): ...
        var b = B(1,2);         |   var b = B(1,2);
    """
    pname = pn.name if pn else None
    while True:
        if pname is None:
            ctor = m if m else default_ctor(())
            return ctor, None
        else:
            pdef = ac[pname]
            ctor_sym = pdef.symtable.get("<init>")
            if ctor_sym and ctor_sym.is_func is True:
                ctor = m if m else default_ctor(ctor_sym.type.param_types)
                return ctor, len(ctor_sym.type.param_types) == 0
            pname = pdef.parent
    pass


def is_left_compare_to_0(left: "Exprs", right: "Expr"):
    return isinstance(left.type, IntType) and isinstance(right, IntLiteral) and right.value == 0


simpl_expr = ExprEval()
expr_gen = ExprGen()


class StmtGen(BaseVisitor):
    def __init__(self, path: str) -> None:
        self.current_CName: str = ""
        self.emit: Emitter = NotImplemented
        self.path = path

    # Non-Expr
    def visitProgram(self, ast: Program, ac: Access):
        [self.visit(cl, ac) for cl in ast.decl]

    def visitClassDecl(self, ast: ClassDecl, ac: Access):
        name = ast.classname.name
        self.current_CName = name
        self.emit = Emitter(self.path + "/" + self.current_CName + ".j")
        ac.emit = self.emit
        ac.enclosing = ast.classname.name

        parent = ast.parentname.name if ast.parentname else ""

        self.emit.printout(self.emit.emitPROLOG(self.current_CName, parent))

        ats, mds, sts, ins, cto = filter_members(ast.memlist)
        [self.visit(a, ac) for a in ats]
        [self.visit(m, ac) for m in mds]

        ctor, pctor_no_args = get_ctor(cto, ast.parentname, ac.globs)

        if "<init>" not in ac.globs[name].symtable:
            fd = FuncDef(
                "<init>", False, FuncType(tuple(p.varType for p in ctor.param), void_t), name
            )
            ac.globs[name].symtable.update({"<init>": fd})
        ctor_obj = CtorObjects(ctor, SelfLiteral(), parent, ins, pctor_no_args)
        genMethod(self, ctor, ctor_obj, ac, ac.frame)

        if sts:
            clinit = MethodDecl(Static(), Id("<clinit>"), [], VoidType(), Block([], []))
            clinit_obj = CtorObjects(clinit, ast.classname, "", sts, None)
            genMethod(self, clinit, clinit_obj, ac, ac.frame)

        self.emit.emitEPILOG()

    def visitAttributeDecl(self, ast: AttributeDecl, ac: Access):
        is_static = isinstance(ast.kind, Static)
        var: "LocalDefType" = self.visit(ast.decl, ac)
        attr = var.to_attr(is_static, self.current_CName)

        self.emit.printout(
            self.emit.emitATTRIBUTE(
                attr.name,
                ast.kind,
                attr.type,
                attr.is_final,
                None,
            )
        )
        return ac.Clone(st=ac.symtable.add(attr))

    def visitVarDecl(self, ast: VarDecl, ac: Access):
        name: str = ast.variable.name
        return LocalVar(name, ast.varType, NotImplemented)

    def visitConstDecl(self, ast: ConstDecl, ac: Access):
        assert ast.value
        name: str = ast.constant.name
        return LocalConst(name, ast.constType, NotImplemented, ast.value)

    def visitMethodDecl(self, ast: MethodDecl, ac: Access):
        genMethod(self, ast, None, ac, ac.frame)

    def visitBlock(self, ast: Block, ac: Access):
        ac.frame.enterScope(False)
        visit_block(self, ast, None, None, ac, ac.frame)
        ac.frame.exitScope()

    def visitIf(self, ast: If, ac: Access):
        exit_label = ac.frame.getNewLabel()
        if_false_label = ac.frame.getNewLabel()
        if_true_label = ac.frame.getNewLabel()
        with ac.flow.enter_block(kind="if"):
            """condition"""
            cond_ast: "Expr" = simpl_expr.visit(ast.expr, ac).ast
            if isinstance(cond_ast, BinaryOp):
                with ac.sc.enter_bool_expr(ac.frame, (if_true_label, if_false_label), "if", True):
                    expr_node: Exprs = expr_gen.visit(cond_ast, ac)
                codes = expr_node.codes
            else:
                expr_node = expr_gen.visit(cond_ast, ac)
                codes = expr_node.codes + (self.emit.emitIF_JUST_FALSE(if_false_label, ac.frame),)
            self.emit.buff.extend(codes)

            self.emit.printout(self.emit.emitLABEL(if_true_label, ac.frame))

            if isinstance(ast.thenStmt, Block):
                self.visit(ast.thenStmt, ac)
            else:
                with ac.flow.enter_block():
                    self.visit(ast.thenStmt, ac)
            if ac.flow.is_reachable and ast.elseStmt:
                self.emit.printout(self.emit.emitGOTO(exit_label, ac.frame))
            self.emit.printout(self.emit.emitLABEL(if_false_label, ac.frame))
            if ast.elseStmt:
                if isinstance(ast.elseStmt, Block):
                    self.visit(ast.elseStmt, ac)
                else:
                    with ac.flow.enter_block():
                        self.visit(ast.elseStmt, ac)

            self.emit.printout(self.emit.emitLABEL(exit_label, ac.frame))

    def visitFor(self, ast: For, ac: Access):
        assign = Assign(ast.id, ast.expr1)
        self.visit(assign, ac)

        ac.frame.enterLoop()

        cond_label = ac.frame.getNewLabel()
        continue_label = ac.frame.getContinueLabel()
        break_label = ac.frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(cond_label, ac.frame))
        rhs = simpl_expr.visit(ast.expr2, ac).ast
        compare_op = "<=" if ast.up else ">="
        cond = BinaryOp(compare_op, ast.id, rhs)
        with ac.sc.enter_bool_expr(ac.frame, (NotImplemented, break_label), "for"):
            cond_code: "Exprs" = expr_gen.visit(cond, ac)
        self.emit.buff.extend(cond_code.codes)

        with ac.flow.enter_block(kind="for"):
            self.visit(ast.loop, ac)

        self.emit.printout(self.emit.emitLABEL(continue_label, ac.frame))
        inc = Assign(ast.id, BinaryOp("+" if ast.up else "-", ast.id, IntLiteral(1)))
        self.visit(inc, ac)
        self.emit.printout(self.emit.emitGOTO(cond_label, ac.frame))

        self.emit.printout(self.emit.emitLABEL(break_label, ac.frame))

        ac.frame.exitLoop()

    def visitContinue(self, ast: Continue, ac: Access):
        ac.flow.handle_continue()
        self.emit.printout(self.emit.emitGOTO(ac.frame.getContinueLabel(), ac.frame))

    def visitBreak(self, ast: Break, ac: Access):
        ac.flow.handle_break()
        self.emit.printout(self.emit.emitGOTO(ac.frame.getBreakLabel(), ac.frame))

    def visitReturn(self, ast: Return, ac: Access):
        ac.flow.mark_unreachable()

        return_expr: "Expr" = simpl_expr.visit(ast.expr, ac).ast
        return_exprs: "Exprs" = expr_gen.visit(return_expr, ac)
        if isinstance(ac.frame.returnType, FloatType) and isinstance(return_exprs.type, IntType):
            codes = return_exprs.codes + (self.emit.emitI2F(ac.frame),)
        else:
            codes = return_exprs.codes
        self.emit.buff.extend(codes)
        assert ac.return_type
        self.emit.printout(self.emit.emitRETURN(ac.return_type, ac.frame))

    def visitAssign(self, ast: Assign, ac: Access):
        visit_assign(self, ast, ac, ac)

    def visitCallStmt(self, ast: CallStmt, ac: Access):
        mname = ast.method.name
        obj_expr = simpl_expr.visit(ast.obj, ac).ast
        obj_node: "TypeDef|Exprs" = expr_gen.visit(obj_expr, ac)
        args_codes: "tuple[str, ...]"
        if obj_node.is_class is True:
            fname = f"{obj_node.name}/{mname}"
            func = obj_node.lookup_member(mname, ac.globs)
            assert isinstance(func, FuncDef)
            args_ast: "map[Expr]" = map(lambda e: simpl_expr.visit(e, ac).ast, ast.param)
            args_codes = reduce(lambda a, e: a + expr_gen.visit(e, ac).codes, args_ast, ())
            codes = args_codes + (ac.emit.emitINVOKESTATIC(fname, func.type, ac.frame),)
        else:
            assert isinstance(obj_node.type, ClassType)
            cls = ac.globs[obj_node.type.classname.name]
            func = cls.lookup_member(mname, ac.globs)
            assert isinstance(func, FuncDef)
            fname = f"{cls.name}/{mname}"

            args_ast = map(lambda e: simpl_expr.visit(e, ac).ast, ast.param)
            args_codes = reduce(lambda a, e: a + expr_gen.visit(e, ac).codes, args_ast, ())

            codes = (
                obj_node.codes
                + args_codes
                + (ac.emit.emitINVOKEVIRTUAL(fname, func.type, ac.frame),)
            )
        self.emit.buff.extend(codes)

    # store expr
    def visitArrayCell(self, ast: ArrayCell, ac: "Access"):
        c: "Access" = ac.Clone(f=Frame(NotImplemented, NotImplemented)) if ac.is_store else ac
        arr_ast: "Expr" = simpl_expr.visit(ast.arr, c).ast

        arr_node: "Exprs" = expr_gen.visit(arr_ast, c)
        assert isinstance(arr_node.type, ArrayType)

        if ac.is_store:
            codes: "tuple[str,...]" = (self.emit.emitASTORE(arr_node.type.eleType, ac.frame),)
            return Exprs(arr_node.ast, arr_node.type.eleType, None, codes)

        idx_ast: "Expr" = simpl_expr.visit(ast.idx, c).ast
        idx_node: "Exprs" = expr_gen.visit(idx_ast, c)
        codes = arr_node.codes + idx_node.codes
        return Exprs(arr_node.ast, arr_node.type.eleType, None, codes)

    def visitFieldAccess(self, ast: FieldAccess, ac: "Access"):
        c: "Access" = ac.Clone(f=Frame(NotImplemented, NotImplemented)) if ac.is_store else ac

        name = ast.fieldname.name
        obj_ast: "Expr" = simpl_expr.visit(ast.obj, c).ast
        obj_node: "TypeDef|Exprs" = expr_gen.visit(obj_ast, c)
        codes: "Tuple[str, ...]"
        if obj_node.is_class is True:
            fname = f"{obj_node.name}.{name}"
            field = obj_node.lookup_member(name, c.globs)
        else:
            assert isinstance(obj_node.type, ClassType)
            _cls_name = obj_node.type.classname.name
            _cls = c.globs[_cls_name]
            field = _cls.lookup_member(name, c.globs)
            fname = f"{_cls_name}.{name}"

        if ac.is_store:
            store = (
                (ac.emit.emitPUTSTATIC(fname, field.type, ac.frame),)
                if obj_node.is_class
                else (ac.emit.emitPUTFIELD(fname, field.type, ac.frame),)
            )
            return Exprs(ast, field.type, None, store)

        codes = () if obj_node.is_class else obj_node.codes
        return Exprs(ast, field.type, None, codes)

    def visitId(self, ast: Id, ac: "Access"):
        s = ac.symtable[ast.name]
        if s.is_var is True:
            assert s.local_index is not None
            codes = (
                (self.emit.emitWRITEVAR(s.name, s.type, s.local_index, ac.frame),)
                if ac.is_store
                else ()
            )
            return Exprs(ast, s.type, None, codes)
        else:
            return s

    # Non uses

    def visitStatic(self, ast: Static, ac: Access):
        pass

    def visitInstance(self, ast: Instance, ac: Access):
        pass

    def visitIntType(self, ast: IntType, ac: Access):
        pass

    def visitFloatType(self, ast: FloatType, ac: Access):
        pass

    def visitBoolType(self, ast: BoolType, ac: Access):
        pass

    def visitStringType(self, ast: StringType, ac: Access):
        pass

    def visitVoidType(self, ast: VoidType, ac: Access):
        pass

    def visitArrayType(self, ast: ArrayType, ac: Access):
        pass

    def visitClassType(self, ast: ClassType, ac: Access):
        pass
