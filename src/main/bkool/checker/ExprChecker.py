from typing import TYPE_CHECKING

from AST import *
from AdditionalTypes import *
from StaticError import *
from Symbolic import *
from TypeCheck import ArrayTypeCheck
from TypeCheker import TypeCheker, Float, Bool, Int, String
from Visitor import BaseVisitor

if TYPE_CHECKING:
    from typing import (
        Final,
        Union,
        Optional,
        Tuple,
        Any,
        List,
        Callable,
        Type as TypeOf,
    )
    from TypeCheck import BkoolTypeCheck, FlexibleTypeCheck
    from typing import NoReturn

__all__ = ["ExprChecker", "throw_undecl"]

IllegalPrimitive = "Primitive type attempted member-access"


def throw_mis(ast: "Expr") -> "NoReturn":
    raise TypeMismatchInExpression(ast)


def throw_undecl(Undeclared_):
    # type: (Union[TypeOf[UndeclaredAttribute], TypeOf[UndeclaredMethod]]) -> Callable[[bool,str],NoReturn]
    def inner(mem_404: "bool", n: "str") -> "NoReturn":
        if mem_404:
            raise Undeclared_(n)
        else:
            raise UndeclaredClass(n)

    return inner


def infer_array_type(
        self: "ExprChecker", ast: "ArrayLiteral", b: "Scoping"
) -> "Tuple[Optional[Type], bool]":
    from TypeCheck import FlexibleTypeCheck

    elt_chk: "FlexibleTypeCheck" = FlexibleTypeCheck(FlexibleType(dyn=True))
    final = True
    for e in ast.value:
        elt: "Union[VarDef, ExprNode]" = self.visit(e, b)
        final = final and elt.is_final
        if elt_chk.assign_from(elt.type, b.globals) is None:
            return None, False
    return ArrayType(len(ast.value), elt_chk.type.inner), final


def eval_binary_op(self, b, op, _left, _right):
    # type: (ExprChecker, Scoping, str, "Union[VarDef, ExprNode]","Union[VarDef, ExprNode]") -> Tuple[Any, bool]
    _left_val = _left.get_value(self, b)
    if _left_val is None:
        return None, False
    elif _left_val is ...:
        return ..., False
    _right_val = _right.get_value(self, b)
    if _right_val is None:
        return None, False
    elif _right_val is ...:
        return ..., False
    try:
        val = eval(f"_left_val {op} _right_val")
    except (TypeError, SyntaxError):
        return None, False
    return val, val is not None and val is not ...


def eval_unary_op(
        self: "ExprChecker",
        b: "Scoping",
        op: "str",
        operand: "Union[VarDef, ExprNode]",
        const: bool,
) -> "Tuple[Any, bool]":
    _value = operand.get_value(self, b)
    if _value is None:
        return None, False
    elif _value is ...:
        return ..., False
    try:
        val = eval(f"{op}_value")
    except (TypeError, SyntaxError):
        return None, False
    return val, const


class ExprChecker(BaseVisitor):
    typechk: "Final" = TypeCheker()

    def check(self, expr: "Expr", b: "Scoping") -> Node:
        return self.visit(expr, b)

    def visitBinaryOp(self, ast: "BinaryOp", b: "Scoping") -> Node:
        left: "Union[VarDef, ExprNode]" = self.visit(ast.left, b)
        right: "Union[VarDef, ExprNode]" = self.visit(ast.right, b)

        if left.is_func or left.is_class:
            raise TypeMismatchInExpression(ast)
        if right.is_func or right.is_class:
            raise TypeMismatchInExpression(ast)

        val = None
        lit = False
        final = left.is_final and right.is_final

        attempt_eval = final and b.visited is not None
        expr_type: "Type"
        chker: "BkoolTypeCheck[Type]"

        if ast.op in ("+", "-", "*"):
            if not isinstance(left.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if not isinstance(right.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)

            if attempt_eval:
                val, lit = eval_binary_op(self, b, ast.op, left, right)

            tupl = ((left.type, Float), (right.type, Float))
            expr_type, chker = next(filter(lambda e: isinstance(e[0], FloatType), tupl), (left.type, Int))

        elif ast.op == "/":
            if not isinstance(left.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if not isinstance(right.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)

            if attempt_eval:
                val, lit = eval_binary_op(self, b, ast.op, left, right)

            expr_type = FloatType()
            chker = Float

        elif ast.op in ("\\", "%"):
            if not (isinstance(left.type, IntType) and isinstance(right.type, IntType)):
                raise TypeMismatchInExpression(ast)
            if attempt_eval:
                py_op = "//" if ast.op == "\\" else ast.op
                val, lit = eval_binary_op(self, b, py_op, left, right)

            expr_type = left.type
            chker = Int

        elif ast.op in ("&&", "||"):
            left_bool = isinstance(left.type, BoolType)
            right_bool = isinstance(right.type, BoolType)
            if not (left_bool and right_bool):
                raise TypeMismatchInExpression(ast)
            if attempt_eval:
                py_op = "and" if ast.op == "&&" else "or"
                val, lit = eval_binary_op(self, b, py_op, left, right)

            expr_type = left.type
            chker = Bool

        elif ast.op in ("==", "!="):
            same_int = type(left.type) is type(right.type) is IntType
            same_bool = type(left.type) is type(right.type) is BoolType
            if not (same_int or same_bool):
                raise TypeMismatchInExpression(ast)
            if attempt_eval:
                val, lit = eval_binary_op(self, b, ast.op, left, right)

            expr_type = BoolType()
            chker = Bool

        elif ast.op in (">", "<", ">=", "<="):
            if not isinstance(left.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if not isinstance(right.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if attempt_eval:
                val, lit = eval_binary_op(self, b, ast.op, left, right)

            expr_type = BoolType()
            chker = Bool

        elif ast.op == "^":
            same_str = type(left.type) is type(right.type) is StringType
            if not same_str:
                raise TypeMismatchInExpression(ast)
            if attempt_eval:
                val, lit = eval_binary_op(self, b, "+", left, right)

            expr_type = left.type
            chker = String
        else:
            assert False, f"Unrecognised binary operator {ast.op}"

        return ExprNode(ast, expr_type, final, lit, val, chker)

    def visitUnaryOp(self, ast: UnaryOp, b: Scoping) -> Node:
        e: "Union[VarDef, ExprNode]" = self.visit(ast.body, b)
        real_val = None
        if e.is_class or e.is_func:
            raise TypeMismatchInExpression(ast)

        attempt_eval = e.is_final and b.visited is not None
        chker: "BkoolTypeCheck[Type]"
        if ast.op in ("+", "-"):
            if not isinstance(e.type, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)

            if attempt_eval:
                real_val, attempt_eval = eval_unary_op(self, b, ast.op, e, attempt_eval)

            chker = Float if isinstance(e.type, FloatType) else Int

        elif ast.op == "!":
            if not isinstance(e.type, BoolType):
                raise TypeMismatchInExpression(ast)

            if attempt_eval:
                real_val, attempt_eval = eval_unary_op(self, b, "not ", e, attempt_eval)

            chker = Bool
            return ExprNode(ast, e.type, e.is_final, attempt_eval, real_val, chker)
        else:
            assert False, f"Unrecognised unary operator {ast.op}"

        return ExprNode(ast, e.type, e.is_final, attempt_eval, real_val, chker)

    def visitCallExpr(self, ast: CallExpr, b: Scoping) -> Node:
        mname = ast.method.name
        obj: "Node" = self.visit(ast.obj, b)

        if obj.is_class is True:
            typedef: TypeDef = obj
            is_static_access = True
        else:
            if not isinstance(obj.type, ClassType):
                raise TypeMismatchInExpression(ast)

            typedef = b.globals[obj.type.classname.name]
            is_static_access = False

        func = typedef.lookup_member(
            mname, b.globals, throw_undecl(UndeclaredMethod), is_static_access
        )

        # if func.is_var is True:
        if func.is_func is False:
            raise UndeclaredMethod(mname)

        if func.is_static is not is_static_access:
            raise IllegalMemberAccess(ast)

        if isinstance(func.type.return_type, VoidType):
            throw_mis(ast)

        args_s: "List[Union[VarDef, ExprNode]]"
        args_s = [self.visit(p, b) for p in ast.param]
        args_t = [throw_mis(ast) if a.is_class else a.type for a in args_s]

        if func.typecheck.not_callable_with(args_t, b.globals):
            throw_mis(ast)

        return_chk = func.typecheck.return_chk
        return ExprNode(ast, func.type.return_type, False, False, None, return_chk)

    def visitNewExpr(self, ast: NewExpr, b: Scoping) -> Node:
        cname = ast.classname.name
        typedef = b.globals.get(cname)
        if typedef is None:
            raise UndeclaredClass(cname)

        args: "List[Union[VarDef, ExprNode]]"
        args = [self.visit(p, b) for p in ast.param]
        args_t = [throw_mis(ast) if a.is_class else a.type for a in args]

        def thrower(_, _____, a=ast):
            return throw_mis(a)

        mems = typedef.lookup_members("<init>", b.globals, thrower)
        while True:
            ctor = next(mems)
            assert ctor.is_func is True
            if ctor.typecheck.callable_with(args_t, b.globals):
                return ExprNode(ast, ClassType(Id(cname)), False, False, None, None)

    def visitArrayCell(self, ast: ArrayCell, b: Scoping) -> Node:
        # base_expr[idx]
        idx_expr: "Union[VarDef, ExprNode]" = self.visit(ast.idx, b)
        if not isinstance(idx_expr.type, IntType):
            raise TypeMismatchInExpression(ast)

        base_expr: "Union[VarDef, ExprNode]" = self.visit(ast.arr, b)
        if not isinstance(base_expr.type, ArrayType):
            raise TypeMismatchInExpression(ast)

        if base_expr._typecheck is not None:
            assert isinstance(base_expr._typecheck, ArrayTypeCheck)
            ele_chker = base_expr._typecheck._ele_chker
        else:
            ele_chker = None
        is_final = (b.is_left and base_expr.is_final) or (
                not b.is_left and base_expr.is_final and idx_expr.is_final
        )
        # Index access is not const
        return ExprNode(ast, base_expr.type.eleType, is_final, False, None, ele_chker)

    def visitFieldAccess(self, ast: FieldAccess, b: Scoping) -> Node:
        obj: "Node" = self.visit(ast.obj, b)
        fname = ast.fieldname.name
        typedef: TypeDef
        if obj.is_class is True:
            typedef = obj
            is_static = True
        elif (obj.is_var or obj.is_expr) and isinstance(obj.type, ClassType):
            assert b.enclosing is not None
            cname = obj.type.classname.name
            contg_cls = b.globals[b.enclosing]
            typedef = contg_cls
            if cname != contg_cls.name and not isinstance(ast.obj, SelfLiteral):
                may_subclass_mro = b.globals[cname].mro(b.globals)
                if contg_cls.name not in may_subclass_mro:
                    raise UndeclaredAttribute(fname)
            is_static = False
        else:
            raise TypeMismatchInExpression(ast)

        field = typedef.lookup_member(
            fname, b.globals, throw_undecl(UndeclaredAttribute), is_static
        )

        if field.is_var is False:
            raise TypeMismatchInExpression(ast)

        if field.is_static is not is_static:
            raise IllegalMemberAccess(ast)

        if b.visited is not None:
            real_val = field.get_value(self, b)
            lit = isinstance(real_val, Literal)
        else:
            real_val, lit = None, False

        return ExprNode(ast, field.type, field.is_final, lit, real_val, field._typecheck)

    def visitIntLiteral(self, ast: IntLiteral, b: Scoping) -> Node:
        return ExprNode(ast, IntType(), True, True, ast.value, Int)

    def visitFloatLiteral(self, ast: FloatLiteral, b: Scoping) -> Node:
        return ExprNode(ast, FloatType(), True, True, ast.value, Float)

    def visitBooleanLiteral(self, ast: BooleanLiteral, b: Scoping) -> Node:
        return ExprNode(ast, BoolType(), True, True, ast.value, Bool)

    def visitStringLiteral(self, ast: StringLiteral, b: Scoping) -> Node:
        return ExprNode(ast, StringType(), True, True, ast.value, String)

    def visitArrayLiteral(self, ast: ArrayLiteral, b: Scoping) -> Node:
        arr_type, final = infer_array_type(self, ast, b)
        if arr_type is None:
            raise TypeMismatchInExpression(ast)
        return ExprNode(ast, arr_type, final, False, None, None)

    def visitNullLiteral(self, ast: NullLiteral, b: Scoping) -> Node:
        return ExprNode(ast, NullType(), True, False, None, None)

    def visitSelfLiteral(self, ast: SelfLiteral, b: Scoping) -> Node:
        assert b.enclosing, "this outside of class"
        assert not b.is_static, "this inside stc method"
        cls = ClassType(Id(b.enclosing))
        return ExprNode(ast, cls, True, False, None, None)

    def visitId(self, ast: Id, b: Scoping) -> Node:
        sym = b.lookup(ast.name)

        if sym is None:
            raise Undeclared(Identifier(), ast.name)
        return sym
