from typing import TYPE_CHECKING, List, Tuple, Optional as Opt, cast

from AST import *
from AdditionalTypes import *
from ReachableBlock import ControlBlock
from StaticError import *
from Symbolic import *
from Symbolic import SymbolTable as St
from TypeCheker import TypeCheker
from Visitor import BaseVisitor

if TYPE_CHECKING:
    from typing import Final
    from TypeCheck import FuncTypeCheck

__all__ = ["FirstPassChecker"]


def visit_block(self, n, pars, bl, s, r, b):
    # type: (FirstPassChecker, str, Opt[List[VarDecl]], Block, bool, Type, Scoping) -> Scoping
    is_block: "Final[bool]" = pars is None
    if is_block:
        if n != "block":
            # n = "true" | "false" block
            b_ = b.BranchDown(tab=St(), stat=s, r=r, fl=b.flow.enter(None, n))
        else:
            b_ = b.BranchDown(tab=St(), stat=s, r=r, fl=b.flow)
            b_.flow.context += "."
    else:
        assert b.enclosing
        enter_method = ControlBlock(f"{b.enclosing}.{n}")
        b_ = b.BranchDown(tab=St(), stat=s, r=r, fl=enter_method)

    for par in (pars if pars is not None else ()):
        try:
            b_ = self.visit(par, b_)
        except Redeclared:
            raise Redeclared(Parameter(), par.variable.name)

    for decl in bl.decl:
        b_ = self.visit(decl, b_)

    merged = b.Clone(stat=s, r=r, tab=b.symtab.merge(b_.symtab), fl=b_.flow)

    for stmt in bl.stmt:
        if merged.flow.is_unreachable:
            print("Unreachable statement: ", stmt)
        merged = self.visit(stmt, merged)

    if is_block:
        if b_.flow is b.flow:  # save 1 level of "method.block..."
            merged.flow.context = merged.flow.context[:-1]
            return merged
        else:
            merged.flow.exit()
            return b
    else:
        # exit in visitMethod
        return merged


def make_block(st: Stmt):
    return st if isinstance(st, Block) else Block([], [st])


def extract_name(m: MemDecl) -> str:
    if isinstance(m, MethodDecl):
        return m.name.name
    _m = cast(AttributeDecl, m)
    if isinstance(_m.decl, VarDecl):
        return _m.decl.variable.name
    else:
        return cast(ConstDecl, _m.decl).constant.name


def attrs_to_assigns(expr: Expr, la: List[AttributeDecl]) -> List[Assign]:
    attr_expr_s = extract_attrs_init(la)
    return [Assign(FieldAccess(expr, Id(ae[0])), ae[1]) for ae in attr_expr_s]


def extract_attrs_init(la: List[AttributeDecl]) -> List[Tuple[str, Expr]]:
    def extract_attr_init(a: AttributeDecl) -> Tuple[str, Opt[Expr]]:
        if isinstance(a.decl, VarDecl):
            return a.decl.variable.name, a.decl.varInit
        else:
            a.decl = cast(ConstDecl, a.decl)
            return a.decl.constant.name, a.decl.value

    raw = [extract_attr_init(a) for a in la]
    filtered: List[Tuple[str, Expr]] = [(e[0], e[1]) for e in raw if e[1] is not None]
    return filtered


class FirstPassChecker(BaseVisitor):
    """raise:
    - Redeclared:
        - Global scope: class name
        - Class scope: method, attr name
        - Method/Block scope: var, const
    - Undeclare identifier in:
        - NameExpr in: # a `name` itself
            - Assignment lhs, possibly rhs # name1 := name2;
            - If # if (name) ...
            - For # for name1 := name2 to name3 { ... }
            - Return # return name;
        - Factors of Biop, UnOp # name1 + name2

        # unchecked.unchecked(name1, name2, ...)
        - Parameters of CallStmt, CallExpr, NewExpr
        - Array Cell # name1[name2]
    - Illegal constant expr: [None init]
    - Not in loop: [break, continue]
    Assert:

    """

    def __init__(self, ast: Program):
        self.ast = ast
        self.typechk = TypeCheker()

    def check(self, b: Scoping) -> Scoping:
        assert b is not None
        return self.visit(self.ast, b)

    def visitProgram(self, ast: Program, b: "Scoping") -> Scoping:
        for decl in ast.decl:
            b = self.visit(decl, b)
        return b

    def visitClassDecl(self, ast: ClassDecl, b: "Scoping") -> "Scoping":
        name = ast.classname.name
        if name in b.symtab:
            raise Redeclared(Class(), name)

        b_ = b.BranchDown(ecls=name)

        for mem_decl in ast.memlist:
            b_ = self.visit(mem_decl, b_)
        # result
        pname = ast.parentname.name if ast.parentname else None
        if pname is None and "<init>" not in b_.symtab:
            sig = FuncType([], VoidType())
            chk: "FuncTypeCheck" = self.typechk.visit(sig, b)
            default_ctor = FuncDef("<init>", True, sig, chk, name)
            b_ = b_.Clone(tab=b_.symtab.add_symbol(default_ctor))
        
        typedef = TypeDef(name, pname, b_.symtab)  # type: ignore
        globs: "GlobalClassTable" = b.symtab.add_symbol(typedef)

        return b.Clone(tab=globs, globs=globs)

    def visitAttributeDecl(self, ast: AttributeDecl, b: "Scoping") -> "Scoping":
        assert b.enclosing is not None
        is_static = isinstance(ast.kind, Static)
        try:
            b_: "Scoping" = b.Clone(stat=is_static)
            b_ = self.visit(ast.decl, b_)
        except Redeclared as ex:
            raise Redeclared(Attribute(), ex.n)
        name = extract_name(ast)

        decl = b_.symtab[name]
        assert decl.is_var is True
        attr = decl.to_attr(is_static, b.enclosing)
        return b.Clone(tab=b.symtab.add_symbol(attr))

    def visitVarDecl(self, ast: VarDecl, b: "Scoping") -> "Scoping":
        name = ast.variable.name
        if name in b.symtab:
            raise Redeclared(Variable(), name)
        """
            class A:                    | class A:
                int a = 0;              |   A():
                int b = a; # a? <Error> |       this.b = a?
                # -> this.a
                void main():
                    int a = 0;
                    int b = a;
        """
        if b.return_type and ast.varInit:
            # In method and has init
            self.visit(ast.varInit, b)
            chk: "BkoolTypeCheck[Type]" = None  # type: ignore
        elif ast.varInit:
            # Is attr and has init
            self.visit(ast.varInit, b.Clone(tab=St()))
            chk = self.typechk.visit(ast.varType, b)
        else:
            chk: "BkoolTypeCheck[Type]" = None  # type: ignore
        var = LocalVar(name, ast.varType, chk)
        return b.Clone(tab=b.symtab.add_symbol(var))

    def visitConstDecl(self, ast: ConstDecl, b: "Scoping") -> "Scoping":
        name = ast.constant.name
        if name in b.symtab:
            raise Redeclared(Variable(), name)
        if ast.value is None:
            raise IllegalConstantExpression(None)
        elif b.return_type:
            self.visit(ast.value, b)
            chk: "BkoolTypeCheck[Type]" = None  # type: ignore
        else:
            self.visit(ast.value, b.Clone(tab=St()))
            chk = self.typechk.visit(ast.constType, b)
        var = LocalConst(name, ast.constType, chk, ast.value)

        return b.Clone(tab=b.symtab.add_symbol(var))

    def visitMethodDecl(self, ast: MethodDecl, b: "Scoping") -> "Scoping":
        assert b.enclosing
        name = ast.name.name

        if name in b.symtab:
            raise Redeclared(Method(), name)
        is_static = isinstance(ast.kind, Static)
        r = VoidType() if ast.returnType is None else ast.returnType

        b_ = visit_block(self, name, ast.param, ast.body, is_static, r, b)

        if b_.flow.reachable and (
                ast.returnType is not None and not isinstance(ast.returnType, VoidType)
        ):
            # raise FunctionNotReturn(ast.name.name)
            print(f"Function {b.enclosing}.{ast.name.name} possibly missing some return statments.")

        sig = FuncType([p.varType for p in ast.param], r)
        chk: "FuncTypeCheck" = self.typechk.visit(sig, b)
        fdef = FuncDef(name, is_static, sig, chk, b.enclosing)
        return b.Clone(tab=b.symtab.add_symbol(fdef))

    def visitBlock(self, ast: Block, b: "Scoping") -> "Scoping":
        assert b.return_type is not None
        return visit_block(self, "block", None, ast, b.is_static, b.return_type, b)

    def visitIf(self, ast: If, b: "Scoping") -> "Scoping":
        assert b.return_type
        self.visit(ast.expr, b)

        enter_if = b.flow.enter(True)

        b_ = b.Clone(fl=enter_if)
        if_bl = make_block(ast.thenStmt)
        visit_block(self, "true", None, if_bl, b.is_static, b.return_type, b_)
        if ast.elseStmt:
            else_bl = make_block(ast.elseStmt)
            visit_block(self, "false", None, else_bl, b.is_static, b.return_type, b_)

        b_.flow.exit()
        return b

    def visitFor(self, ast: For, b: "Scoping") -> "Scoping":
        self.visit(ast.id, b)
        self.visit(ast.expr1, b)
        self.visit(ast.expr2, b)

        enter_for = b.flow.enter(False)
        b_ = b.Clone(depth=b.loop_depth + 1, fl=enter_for)
        self.visit(ast.loop, b_)
        b_.flow.exit()

        return b

    def visitContinue(self, ast: Continue, b: "Scoping") -> "Scoping":
        if b.loop_depth == 0:
            raise MustInLoop(ast)
        b.flow.continue_()
        return b

    def visitBreak(self, ast: Break, b: "Scoping") -> "Scoping":
        if b.loop_depth == 0:
            raise MustInLoop(ast)
        b.flow.break_()
        return b

    def visitReturn(self, ast: Return, b: "Scoping") -> "Scoping":
        self.visit(ast.expr, b)
        b.flow.mark_unreachable()
        return b

    def visitAssign(self, ast: Assign, b: "Scoping") -> "Scoping":
        self.visit(ast.lhs, b)
        self.visit(ast.exp, b)
        return b

    def visitCallStmt(self, ast: CallStmt, b: "Scoping") -> "Scoping":
        [self.visit(p, b) for p in ast.param]
        return b

    # Some visitExpr may return None due to being not implemented
    def visitArrayCell(self, ast: ArrayCell, b: "Scoping") -> "Scoping":
        self.visit(ast.arr, b)
        self.visit(ast.idx, b)
        return b

    def visitBinaryOp(self, ast: BinaryOp, b: "Scoping") -> "Scoping":
        self.visit(ast.left, b)
        self.visit(ast.right, b)
        return b

    def visitUnaryOp(self, ast: UnaryOp, b: "Scoping") -> "Scoping":
        self.visit(ast.body, b)
        return b

    def visitCallExpr(self, ast: CallExpr, b: "Scoping") -> "Scoping":
        [self.visit(p, b) for p in ast.param]
        return b

    def visitNewExpr(self, ast: NewExpr, b: "Scoping") -> "Scoping":
        [self.visit(p, b) for p in ast.param]
        return b

    def visitId(self, ast: Id, b: "Scoping") -> "Scoping":
        if b.exist(ast.name):
            return b
        else:
            raise Undeclared(Identifier(), ast.name)
