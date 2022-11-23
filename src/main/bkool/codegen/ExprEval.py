import sys

sys.path.append("./target/")
sys.path.append("./src/test/")
sys.path.append("./src/main/bkool/parser/")
sys.path.append("./src/main/bkool/utils/")
sys.path.append("./src/main/bkool/astgen/")
sys.path.append("./src/main/bkool/checker/")
sys.path.append("./src/main/bkool/codegen/")

from typing import Any, Optional as Opt, Union, List, TYPE_CHECKING

from AST import *
from AdditionalTypes import AnyType, NullType, ArraysOfDefault
from Visitor import BaseVisitor
from CodeGenSymbol import (
    Access,
    Exprs,
    Node,
    VarDefGeneric,
    TypeDef,
    GlobalClassTable,
)

if TYPE_CHECKING:
    Primitive = Union[IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral]

str_t = StringType()
int_t = IntType()
float_t = FloatType()
bool_t = BoolType()
void_t = VoidType()
null_t = NullType()
any_t = AnyType()


def Lit(left: Any, right: Any, op: "Opt[str]" = None) -> Any:
    if left is None:
        return right
    elif op in ("<", ">", "<=", ">=", "==", "!="):
        return BooleanLiteral
    elif op == "/":
        return FloatLiteral
    else:
        return FloatLiteral if FloatLiteral in (left, right) else left


def aggregate_type(left: Any, right: Any, op: "Opt[str]" = None) -> Any:
    if left is None:
        return right
    elif op in ("<", ">", "<=", ">=", "==", "!="):
        return bool_t
    elif op == "/":
        return float_t
    else:
        return float_t if any(isinstance(e, FloatType) for e in (left, right)) else left


def type_aggregate(left: "Opt[Type]", right: "Type", gl: "GlobalClassTable"):
    if left is None:
        return right
    if FloatType in (type(left), type(right)):
        return float_t
    elif isinstance(left, ClassType) and isinstance(right, ClassType):
        name = right.classname.name
        if name == left.classname.name:
            return left
        rhs = gl[left.classname.name]
        parent = rhs.parent
        while parent:
            parent_cls = gl[parent]
            if parent_cls.name == name:
                return right
            parent = parent_cls.parent
    return left


def is_primitive_type(type_: Type):
    return isinstance(type_, (IntType, FloatType, StringType, BoolType))


def is_literal(expr: Expr):
    return isinstance(expr, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral))


def eval_binexpr(op: str, left: "Primitive|Any", right: "Primitive|Any"):
    try:
        if op == "^":
            assert isinstance(left, StringLiteral)
            assert isinstance(right, StringLiteral)
            return f'"{eval(f"{repr(left.value[1:-1])} + {repr(right.value[1:-1])}")}"'
        else:
            pyop = "and" if op == "&&" else "or" if op == "||" else op
            return eval(f"{repr(left.value)} {pyop} {repr(right.value)}")
    except Exception:
        return None


def eval_unexpr(op: str, body: "Primitive"):
    pyop = "not" if op == "!" else op
    try:
        return eval(f"{pyop} {body.value}")
    except Exception:
        return None


class ExprEval(BaseVisitor):
    @staticmethod
    def visitArraysOfDefault(ast: ArraysOfDefault, __: Access):
        return Exprs(ast, ast.array_type)

    def visitBinaryOp(self, ast: BinaryOp, ac: Access):
        left: "Exprs|VarDefGeneric" = self.visit(ast.left, ac)
        right: "Exprs|VarDefGeneric" = self.visit(ast.right, ac)
        type_ = aggregate_type(left.type, right.type, ast.op)
        if left.has_literal_value and right.has_literal_value:
            val = eval_binexpr(ast.op, left.ast, right.ast)
            Cls = Lit(type(left.ast), type(right.ast), ast.op)
            if val is not None:
                return Exprs(Cls(val), type_, True)

        return Exprs(BinaryOp(ast.op, left.ast, right.ast), type_, False)

    def visitUnaryOp(self, ast: UnaryOp, ac: Access):
        body: "Exprs|VarDefGeneric" = self.visit(ast.body, ac)
        if body.has_literal_value:
            if ast.op == "-" and isinstance(body.ast, (IntLiteral, FloatLiteral)):
                val = eval_unexpr("-", body.ast)
                if val is not None:
                    return Exprs(type(body.ast)(val), body.type, True)
            elif ast.op == "!" and isinstance(body.ast, BooleanLiteral):
                val = eval_unexpr("!", body.ast)
                if val is not None:
                    return Exprs(BooleanLiteral(val), bool_t, True)
        return Exprs(UnaryOp(ast.op, body.ast), body.type, False)

    def visitCallExpr(self, ast: CallExpr, ac: Access):
        cls: TypeDef
        obj_e: Union[TypeDef, VarDefGeneric, Exprs] = self.visit(ast.obj, ac)
        if obj_e.is_class is True:
            cls = obj_e
        else:
            assert obj_e.is_var or obj_e.is_expr
            assert isinstance(obj_e.type, ClassType)
            _cls_or_var = ac.globs[obj_e.type.classname.name]
            assert _cls_or_var.is_class
            cls = _cls_or_var
        mem = cls.lookup_member(ast.method.name, ac.globs)
        assert mem.is_func is True
        args: List[Expr] = [self.visit(a, ac).ast for a in ast.param]
        new_call = CallExpr(obj_e.ast, ast.method, args)
        return Exprs(new_call, mem.type.return_type, False)

    def visitNewExpr(self, ast: NewExpr, ac: Access):
        args: List[Expr] = [self.visit(a, ac).ast for a in ast.param]
        new_expr = NewExpr(ast.classname, args)
        return Exprs(new_expr, ClassType(ast.classname), False)

    def visitArrayCell(self, ast: ArrayCell, ac: Access):
        arr_expr: Exprs = self.visit(ast.arr, ac)
        idx_expr: Exprs = self.visit(ast.idx, ac)
        arr_cell = ArrayCell(arr_expr.ast, idx_expr.ast)
        assert isinstance(arr_expr.type, ArrayType)
        return Exprs(arr_cell, arr_expr.type.eleType, False)

    def visitFieldAccess(self, ast: FieldAccess, ac: Access):
        cls: TypeDef
        obj_e: Union[TypeDef, VarDefGeneric, Exprs] = self.visit(ast.obj, ac)
        if obj_e.is_class is True:
            cls = obj_e
        else:
            assert obj_e.is_var or obj_e.is_expr
            assert isinstance(obj_e.type, ClassType)
            _cls_or_var = ac.globs[obj_e.type.classname.name]
            assert _cls_or_var.is_class
            cls = _cls_or_var
        mem = cls.lookup_member(ast.fieldname.name, ac.globs)
        assert mem.is_var is True
        if mem.is_final and is_primitive_type(mem.type):
            v = mem.get_ast_value(self, ac)
            if v is not None:
                return Exprs(v, mem.type, True)
            else:
                return Exprs(FieldAccess(obj_e.ast, ast.fieldname), mem.type, False)

        return Exprs(FieldAccess(obj_e.ast, ast.fieldname), mem.type, False)

    def visitIntLiteral(self, ast: IntLiteral, ac: Access):
        return Exprs(ast, int_t, True)

    def visitFloatLiteral(self, ast: FloatLiteral, ac: Access):
        return Exprs(ast, float_t, True)

    def visitBooleanLiteral(self, ast: BooleanLiteral, ac: Access):
        return Exprs(ast, bool_t, True)

    def visitStringLiteral(self, ast: StringLiteral, ac: Access):
        return Exprs(ast, str_t, True)

    def visitArrayLiteral(self, ast: ArrayLiteral, ac: Access):
        glob: "GlobalClassTable" = dict() if ac is None else ac.globs  # type: ignore
        arr_len = len(ast.value)
        buff: "List[Any]" = []
        ele_type: "Type" = None  # type: ignore
        for e in ast.value:
            node: "Exprs" = self.visit(e, ac)
            ele_type = type_aggregate(ele_type, node.type, glob)
            value = node.get_ast_value(self, ac)
            if value is not None:
                buff.append(value)
            else:
                buff.append(e)
        array_lit = ArrayLiteral(buff)
        return Exprs(array_lit, ArrayType(arr_len, ele_type), None)

    def visitNullLiteral(self, ast: NullLiteral, ac: Access):
        return Exprs(ast, null_t, False)

    def visitSelfLiteral(self, ast: SelfLiteral, ac: Access):
        assert ac.enclosing
        return Exprs(ast, ClassType(Id(ac.enclosing)), False)

    def visitId(self, ast: Id, ac: Access) -> "Node":
        sym = ac.symtable[ast.name]
        if sym.is_var is True:
            if sym.is_final and is_primitive_type(sym.type):
                ast_val = sym.get_ast_value(self, ac)
                if ast_val is not None:
                    return Exprs(ast_val, sym.type, True)
            return sym
        else:
            return sym
