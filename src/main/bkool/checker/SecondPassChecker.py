from typing import Optional, Union, List, Tuple, TYPE_CHECKING

from AST import *
from ExprChecker import ExprChecker, throw_undecl
from StaticError import *
from Symbolic import *
from Symbolic import SymbolTable as ST
from TypeCheck import BkoolTypeCheck
from TypeCheker import TypeCheker
from Visitor import BaseVisitor

if TYPE_CHECKING:
    from typing import NoReturn, Any

__all__ = ["SecondPassChecker"]


def throw(ex: "Exception") -> "NoReturn":
    raise ex


def visit_block(self, pars, bl, s, r, b):
    # type: (SecondPassChecker, Optional[List[Any]], Block, bool, Type, Scoping) -> Scoping
    if pars is None:
        b_ = b.BranchDown(stat=s, r=r)
    else:
        b_ = b.BranchDown(tab=ST(), stat=s, r=r)

    decls: "List[StoreDecl]" = pars + bl.decl if pars is not None else bl.decl
    for decl in decls:
        b_ = self.visit(decl, b_)

    merged = b.Clone(stat=s, r=r, tab=b.symtab.merge(b_.symtab))

    for stmt in bl.stmt:
        merged = self.visit(stmt, merged)

    return b


class SecondPassChecker(BaseVisitor):
    def __init__(self, ast: Program):
        self.ast = ast
        self.expr = ExprChecker()
        self.typechk = TypeCheker()

    def check(self, b: Scoping) -> Scoping:
        assert b is not None
        return self.visit(self.ast, b)

    def visitProgram(self, ast: Program, b: Scoping) -> Scoping:
        for decl in ast.decl:
            b = self.visit(decl, b)

        return b

    def visitClassDecl(self, ast: ClassDecl, b: Scoping) -> Scoping:
        typedef = b.globals[ast.classname.name]
        if typedef.parent and b.globals.get(typedef.parent) is None:
            raise Undeclared(Class(), typedef.parent)

        b_ = b.BranchDown(ecls=ast.classname.name)
        for mem_decl in ast.memlist:
            b_ = self.visit(mem_decl, b_)

        return b

    def visitAttributeDecl(self, ast: AttributeDecl, b: Scoping) -> Scoping:
        assert b.enclosing is not None
        static = isinstance(ast.kind, Static)
        b_ = b.Clone(stat=static)
        self.visit(ast.decl, b_)

        return b

    def visitVarDecl(self, ast: VarDecl, b: Scoping) -> Scoping:
        name = ast.variable.name
        
        expr: Optional[Node] = None
        if ast.varInit:
            if b.return_type:  # local
                env = b.Clone(v=None)
                chk = self.typechk.visit(ast.varType, None)
            else:  # In class
                assert b.enclosing
                this_class: TypeDef = b.globals[b.enclosing]
                field_sym = this_class.symtable[name]
                chk = field_sym.typecheck

                env = b.Clone(stat=field_sym.is_static, tab=ST(), v=None)
            
            expr = self.expr.check(ast.varInit, env)
            assign = Assign(Id(ast.variable.name), ast.varInit)
            if expr.is_class is True or expr.is_func is True:
                raise TypeMismatchInExpression(assign)
            
            if chk.assign_from(expr.type, b.globals) is None:
                raise TypeMismatchInExpression(assign)
        else:
            chk = self.typechk.visit(ast.varType, None)

        var = LocalVar(name, ast.varType, chk)

        return b.Clone(tab=b.symtab.add_symbol(var))

    def visitConstDecl(self, ast: ConstDecl, b: Scoping) -> Scoping:
        name = ast.constant.name
        assert ast.value is not None
        chk: BkoolTypeCheck[Type]
        expr: Node
        if b.return_type:
            chk = self.typechk.visit(ast.constType, None)
            env = b.Clone(v=())
        else:
            assert b.enclosing
            this_class: TypeDef = b.globals[b.enclosing]
            field = this_class.symtable[name]
            chk = field.typecheck

            this_attr: Tuple[str, str]
            this_attr = this_class.name, ast.constant.name

            env = b.Clone(stat=field.is_static, tab=ST(), v=(this_attr,))

        expr = self.expr.visit(ast.value, env)
        mismatch = TypeMismatchInConstant(ast)

        if expr.is_var is False and expr.is_expr is False:
            raise mismatch
        
        if expr.is_final is False:
            raise IllegalConstantExpression(ast.value)
        literal_value = expr.get_value(self.expr, b)
        if literal_value is ...:
            if b.return_type:
                print(f"Circular init in local {ast.constant.name}")
            elif b.enclosing:
                print(f"Circular init in {b.enclosing}.{ast.constant.name}")

        if chk.assign_from(expr.type, b.globals) is None:
            raise mismatch

        var = LocalConst(name, ast.constType, chk, expr.ast_value)

        return b.Clone(tab=b.symtab.add_symbol(var))

    def visitMethodDecl(self, ast: MethodDecl, b: Scoping) -> Scoping:
        if ast.name.name == "<init>":
            assert b.enclosing
            typedef = b.globals[b.enclosing]

            if typedef.parent is not None:
                ctors = typedef.lookup_members("<init>", b.globals, throw_undecl(UndeclaredMethod))
                current = next(ctors)
                assert current.is_func
                parent = next(ctors)
                assert parent.is_func is True
                if parent.type.param_types and not current.typecheck.is_same_type(parent.type):
                    # This will bite you in codegen
                    # Parent() no args is okay
                    raise TypeMismatchInExpression("Constructor Incompatible!")

        st = isinstance(ast.kind, Static)
        r = VoidType() if ast.returnType is None else ast.returnType
        visit_block(self, ast.param, ast.body, st, r, b)

        return b

    def visitBlock(self, ast: Block, b: Scoping) -> Scoping:
        assert b.return_type is not None
        return visit_block(self, None, ast, b.is_static, b.return_type, b)

    def visitIf(self, ast: If, b: Scoping) -> Scoping:
        cond: Node = self.expr.visit(ast.expr, b)
        if cond.is_class is True or cond.is_func is True:
            raise TypeMismatchInStatement(ast)

        if not isinstance(cond.type, BoolType):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt, b)
        self.visit(ast.elseStmt, b) if ast.elseStmt else None
        return b

    def visitFor(self, ast: For, b: Scoping) -> Scoping:
        it: Node = self.expr.visit(ast.id, b)
        expr1: Node = self.expr.visit(ast.expr1, b)
        expr2: Node = self.expr.visit(ast.expr2, b)

        if (
            it.is_class is True
            or it.is_func is True
            or expr1.is_class is True
            or expr1.is_func is True
            or expr2.is_class is True
            or expr2.is_func is True
        ):
            raise TypeMismatchInStatement(ast)


        if any(not isinstance(e.type, IntType) for e in (it, expr1, expr2)):
            raise TypeMismatchInStatement(ast)
        b_ = b.Clone(depth=b.loop_depth + 1)
        self.visit(ast.loop, b_)
        return b

    def visitContinue(self, ast: Continue, b: Scoping) -> Scoping:
        return b

    def visitBreak(self, ast: Break, b: Scoping) -> Scoping:
        return b

    def visitReturn(self, ast: Return, b: Scoping) -> Scoping:
        retval: Union[VarDef, ExprNode] = self.expr.visit(ast.expr, b)
        if retval.is_class is True:
            raise TypeMismatchInStatement(ast)
        assert b.return_type
        if retval.typecheck.assign_to(b.return_type, b.globals) is None:
            raise TypeMismatchInStatement(ast)
        return b

    def visitAssign(self, ast: Assign, b: Scoping) -> Scoping:
        bleft = b.Clone(lhs=True)
        lhs: Union[VarDef, ExprNode] = self.expr.visit(ast.lhs, bleft)
        if lhs.is_class:
            raise TypeMismatchInStatement(ast)
        if lhs.is_final:
            raise CannotAssignToConstant(ast)
        rhs: Union[VarDef, ExprNode] = self.expr.visit(ast.exp, b)
        if rhs.is_class:
            raise TypeMismatchInStatement(ast)

        if lhs.typecheck.assign_from(rhs.type, b.globals) is None:
            raise TypeMismatchInStatement(ast)

        return b

    def visitCallStmt(self, ast: CallStmt, b: Scoping) -> Scoping:
        mname = ast.method.name
        sym: Symbol = self.expr.visit(ast.obj, b)

        if sym.is_class is True:
            typedef: TypeDef = sym
            is_static_access = True
        else:
            if not isinstance(sym.type, ClassType):
                raise TypeMismatchInExpression(ast)

            typedef = b.globals[sym.type.classname.name]
            is_static_access = False

        # Don't access a static member that is defined
        # in a base class from a derived class.
        # Even though it is possible, just no.
        func = typedef.lookup_member(
            mname, b.globals, throw_undecl(UndeclaredMethod), is_static_access
        )

        if func.is_func is False:
            # mname is a field or None, raise what now?
            raise UndeclaredMethod(mname)

        ex = TypeMismatchInExpression(ast)
        
        if func.is_static is not is_static_access:
            raise IllegalMemberAccess(ast)

        if not isinstance(func.type.return_type, VoidType):
            raise ex

        args_s: List[Union[VarDef, ExprNode]]

        args_s = [self.expr.visit(p, b) for p in ast.param]
        args_t = [throw(ex) if a.is_class else a.type for a in args_s]

        args_valid = func.typecheck.callable_with(args_t, b.globals)
        if not args_valid:
            raise ex

        return b
