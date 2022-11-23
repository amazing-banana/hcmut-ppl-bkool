import sys

sys.path.append("./target/")
sys.path.append("./src/test/")
sys.path.append("./src/main/bkool/parser/")
sys.path.append("./src/main/bkool/utils/")
sys.path.append("./src/main/bkool/astgen/")
sys.path.append("./src/main/bkool/checker/")
sys.path.append("./src/main/bkool/codegen/")

from functools import reduce

from typing import Optional as Opt, List, Tuple, TYPE_CHECKING

from Emitter import Emitter  # type: ignore

from CodeGenError import IllegalOperandException
from CodeGenSymbol import FuncDef
from Frame import Frame
from Visitor import BaseVisitor

from CodeGenSymbol import Access, Exprs, Node, TypeDef
from AdditionalTypes import FuncType, NullType, ArraysOfDefault, FlexibleType, AnyType, AnyRefType
from AST import *

if TYPE_CHECKING:
    from typing import Any

    pass

str_t = StringType()
int_t = IntType()
float_t = FloatType()
bool_t = BoolType()
void_t = VoidType()
null_t = NullType()


def flatten(ast: "Expr", op: "str") -> "tuple[Expr,...]":
    if isinstance(ast, BinaryOp) and ast.op == op:
        return flatten(ast.left, op) + flatten(ast.right, op)
    else:
        return (ast,)


def emit_string_concat(self, ast, ac):
    # type: (ExprGen, Expr, Access) -> tuple[str,...]
    exprs = flatten(ast, "^")
    builder_class = ClassType(Id("java/lang/StringBuilder"))
    builder_ctor = "java/lang/StringBuilder/<init>"
    builder_ctor_proto = FuncType([], VoidType())
    append = "java/lang/StringBuilder/append"
    append_proto = FuncType([StringType()], builder_class)
    toString = "java/lang/StringBuilder/toString"
    toString_proto = FuncType([], StringType())

    buff: "List[str]" = [
        ac.emit.emitNEW(builder_class, ac.frame),
        ac.emit.emitDUP(ac.frame),
        ac.emit.emitINVOKESPECIAL(ac.frame, builder_ctor, builder_ctor_proto),
    ]

    for e in exprs:
        expr_node: "Exprs" = self.visit(e, ac)
        buff.extend(expr_node.codes)
        buff.append(ac.emit.emitINVOKEVIRTUAL(append, append_proto, ac.frame))

    buff.append(ac.emit.emitINVOKEVIRTUAL(toString, toString_proto, ac.frame))
    return tuple(buff)


def short_circut_and_or(self, ast, ac):
    # type: (ExprGen, BinaryOp, Access) -> tuple[str,...]
    buff: "List[str]" = []
    current_root_and = ast.op == "&&"
    ast_exprs = flatten(ast, ast.op)

    true_label, false_label = ac.sc.get_current_labels()

    next_expr_label: "Opt[int]" = None

    for e in ast_exprs[:-1]:
        expr_node: "Exprs"
        if next_expr_label is not None:
            buff.append(ac.emit.emitLABEL(next_expr_label, ac.frame))

        if isinstance(e, BinaryOp) and e.op in ("||", "&&", ">", ">=", "<", "<=", "!=", "=="):
            next_expr_label = ac.frame.getNewLabel()

            if current_root_and:
                if_sub_true, if_sub_false = next_expr_label, false_label
            else:
                if_sub_true, if_sub_false = true_label, next_expr_label

            with ac.sc.push_label_context(if_sub_true, if_sub_false):
                expr_node = self.visit(e, ac)
            buff.extend(expr_node.codes)
        elif isinstance(e, UnaryOp) and e.op == "!":
            next_expr_label = None
            with ac.sc.push_label_context(true_label, false_label):
                expr_node = self.visit(e, ac)
            buff.extend(expr_node.codes)
        else:
            next_expr_label = None
            with ac.sc.enter_expr():
                expr_node = self.visit(e, ac)
            buff.extend(expr_node.codes)
            buff.append(ac.emit.and_or_jump(current_root_and, true_label, false_label, ac))
    else:
        last = ast_exprs[-1]
        if next_expr_label is not None:
            buff.append(ac.emit.emitLABEL(next_expr_label, ac.frame))
        assert true_label != false_label
        with ac.sc.push_label_context(true_label, false_label, last=True):
            and_or_rel = isinstance(last, BinaryOp) and last.op in (
                "||",
                "&&",
                ">",
                ">=",
                "<",
                "<=",
                "!=",
                "==",
            )
            neg = isinstance(last, UnaryOp) and last.op == "!"
            if and_or_rel or neg:
                expr_node = self.visit(last, ac)
            else:
                with ac.sc.enter_expr():
                    expr_node = self.visit(last, ac)
            buff.extend(expr_node.codes)
            if not and_or_rel:
                if neg and ac.sc.absolute_last():
                    code = ac.emit.emitNEGATE(false_label, true_label, ac, False)
                    buff.append(code)
                else:
                    code = ac.emit.and_or_jump(current_root_and, true_label, false_label, ac, True)
                    buff.append(code)

    return tuple(buff)


def is_left_compare_to_0(left: "Exprs", right: "Expr"):
    return isinstance(left.type, IntType) and isinstance(right, IntLiteral) and right.value == 0


def emitBool(
    cond: "bool",
    emit: "Emitter",
    true_label: "int",
    false_label: "int",
    frame: "Frame",
    push: "bool" = False,
) -> "Tuple[str, ...]":
    if cond:
        return (
            emit.emitLABEL(false_label, frame),
            emit.emitPUSHICONST(0, frame) if push else emit.jvm.emitICONST(0),
        )
    else:
        return (
            emit.emitLABEL(true_label, frame),
            emit.emitPUSHICONST(1, frame) if push else emit.jvm.emitICONST(1),
        )


class ExprGen(BaseVisitor):
    @staticmethod
    def visitArraysOfDefault(ast: ArraysOfDefault, ac: Access):
        codes: "Tuple[str, ...]"
        if isinstance(ast.array_type.eleType, ArrayType):
            codes = (ac.emit.emit_ARRAY_ALLOC_MULTI_ANEARRAY(ast.array_type, ac.frame),)
        else:
            codes = (ac.emit.emit_ARRAY_ALLOC_ANEWARRAY(ast.array_type, ac.frame),)
        return Exprs(ast, ast.array_type, False, codes)

    def visitBinaryOp(self, ast: BinaryOp, ac: Access):
        codes: "tuple[str, ...]"
        if ast.op == "^":
            codes = emit_string_concat(self, ast, ac)
            return Exprs(ast, str_t, None, codes)

        elif ast.op in ("&&", "||"):
            with ac.sc.enter_bool_expr(ac.frame, None, ast.op) as (true_label, false_label):
                codes = short_circut_and_or(self, ast, ac)
                if ac.sc.is_current_root():
                    escape_label_ = ac.frame.getNewLabel()
                    first_value_ = emitBool(
                        ast.op == "||", ac.emit, true_label, false_label, ac.frame
                    )
                    escape_jump_ = (ac.emit.emitGOTO(escape_label_, ac.frame),)
                    second_value_ = emitBool(
                        ast.op == "&&", ac.emit, true_label, false_label, ac.frame, True
                    )
                    exit_jump_ = (ac.emit.emitLABEL(escape_label_, ac.frame),)
                    emit_boolean: "Tuple[str, ...]" = (
                        first_value_ + escape_jump_ + second_value_ + exit_jump_
                    )
                else:
                    emit_boolean = ()
            return Exprs(ast, str_t, None, codes + emit_boolean)

        elif ast.op in (">", ">=", "<", "<=", "!=", "=="):
            with ac.sc.enter_bool_expr(ac.frame, None, ast.op) as (true_label, false_label):
                left: "Exprs" = self.visit(ast.left, ac)
                right: "Exprs"

                if is_left_compare_to_0(left, ast.right):
                    jump = (ac.emit.compare_to_0(ast.op, true_label, false_label, ac),)
                    codes = left.codes + jump
                else:
                    right = self.visit(ast.right, ac)

                    if isinstance(left.type, IntType) and isinstance(right.type, IntType):
                        jump = (ac.emit.int_compare(ast.op, true_label, false_label, ac),)
                        codes = left.codes + right.codes + jump
                    else:
                        left_code = (
                            (left.codes + (ac.emit.emitI2F(ac.frame),))
                            if isinstance(left.type, IntType)
                            else left.codes
                        )
                        right_code = (
                            (right.codes + (ac.emit.emitI2F(ac.frame),))
                            if isinstance(right.type, IntType)
                            else right.codes
                        )
                        jump = (ac.emit.float_compare(ast.op, true_label, false_label, ac),)

                        codes = left_code + right_code + jump

                if ac.sc.is_current_root():
                    escape_label = ac.frame.getNewLabel()
                    emit_boolean = (
                        ac.emit.emitLABEL(true_label, ac.frame),
                        ac.emit.emitPUSHICONST(1, ac.frame),
                        ac.emit.emitGOTO(escape_label, ac.frame),
                        ac.emit.emitLABEL(false_label, ac.frame),
                        ac.emit.jvm.emitICONST(0),
                        ac.emit.emitLABEL(escape_label, ac.frame),
                    )
                else:
                    emit_boolean = ()

            return Exprs(ast, bool_t, None, codes + emit_boolean)
        else:
            left = self.visit(ast.left, ac)
            right = self.visit(ast.right, ac)
            left_code = left.codes
            right_code = right.codes

            expr_type = left.type

            left_float = isinstance(left.type, FloatType)
            right_float = isinstance(right.type, FloatType)

            if left_float or right_float or ast.op == "/":
                if not left_float:
                    left_code = left_code + (ac.emit.emitI2F(ac.frame),)
                if not right_float:
                    right_code = right_code + (ac.emit.emitI2F(ac.frame),)
                expr_type = float_t

            if ast.op in ("+", "-"):
                codes = left_code + right_code + (ac.emit.emitADDOP(ast.op, expr_type, ac.frame),)
            elif ast.op in ("*", "/"):
                codes = left_code + right_code + (ac.emit.emitMULOP(ast.op, expr_type, ac.frame),)
            elif ast.op == "\\":
                codes = left_code + right_code + (ac.emit.emitDIV(ac.frame),)
            elif ast.op == "%":
                codes = left_code + right_code + (ac.emit.emitMOD(ac.frame),)
            else:
                raise IllegalOperandException(f"Unknown biop {ast.op}")

            return Exprs(ast, expr_type, None, codes)

    def visitUnaryOp(self, ast: UnaryOp, ac: Access):
        codes: "tuple[str, ...]"
        e: "Exprs"
        if ast.op == "!":
            with ac.sc.enter_bool_expr(ac.frame, None, "!") as (true_label, false_label):
                if ac.sc.is_current_root():  # var a = !(...)
                    escape_label = ac.frame.getNewLabel()
                    with ac.sc.enter_expr():
                        e = self.visit(ast.body, ac)
                    codes = e.codes + (
                        ac.emit.emit_jump_if_true(false_label, ac.frame),
                        ac.emit.emitPUSHCONST("true", bool_t, ac.frame),
                        ac.emit.emitGOTO(escape_label, ac.frame),
                        ac.emit.emitLABEL(false_label, ac.frame),
                        ac.emit.emitPUSHCONST("false", bool_t, ac.frame),
                        ac.emit.emitLABEL(escape_label, ac.frame),
                    )
                else:
                    with ac.sc.enter_expr():
                        e = self.visit(ast.body, ac)
                    codes = e.codes + (ac.emit.emitNEGATE(true_label, false_label, ac),)
            return Exprs(ast, bool_t, None, codes)

        elif ast.op == "-":
            e = self.visit(ast.body, ac)
            codes = e.codes + (ac.emit.emitNEGOP(e.type, ac.frame),)
            return Exprs(ast, e.type, None, codes)
        raise IllegalOperandException(f"Unknown unary {ast.op}")

    def visitCallExpr(self, ast: CallExpr, ac: Access):
        mname = ast.method.name
        obj_node: "TypeDef|Exprs" = self.visit(ast.obj, ac)
        args_codes: "tuple[str, ...]"
        if obj_node.is_class is True:
            fname = f"{obj_node.name}/{mname}"
            func = obj_node.lookup_member(mname, ac.globs)
            assert isinstance(func, FuncDef)
            args_codes = reduce(lambda a, e: a + self.visit(e, ac).codes, ast.param, ())
            codes = args_codes + (ac.emit.emitINVOKESTATIC(fname, func.type, ac.frame),)
        else:
            assert isinstance(obj_node.type, ClassType)
            cls = ac.globs[obj_node.type.classname.name]
            func = cls.lookup_member(mname, ac.globs)
            assert isinstance(func, FuncDef)
            fname = f"{cls.name}/{mname}"

            args_codes = reduce(lambda a, e: a + self.visit(e, ac).codes, ast.param, ())

            codes = (
                obj_node.codes
                + args_codes
                + (ac.emit.emitINVOKEVIRTUAL(fname, func.type, ac.frame),)
            )

        return Exprs(ast, func.type.return_type, None, codes)

    def visitNewExpr(self, ast: NewExpr, ac: Access):
        cname = ast.classname.name
        init = (
            ac.emit.emitNEW(ClassType(Id(cname)), ac.frame),
            ac.emit.emitDUP(ac.frame),
        )
        codes: "Tuple[str,...]" = ()
        types: "Tuple[Type,...]" = ()

        for arg in ast.param:
            _exprs: "Exprs" = self.visit(arg, ac)
            codes = codes + _exprs.codes
            types = types + (_exprs.type,)

        mname = ast.classname.name + "/<init>"

        invoke = ac.emit.emitINVOKESPECIAL(ac.frame, mname, FuncType(types, void_t))
        expr_type = ClassType(ast.classname)
        return Exprs(ast, expr_type, None, init + codes + (invoke,))

    def visitArrayCell(self, ast: ArrayCell, ac: Access):
        arr_node: "Exprs" = self.visit(ast.arr, ac)
        assert isinstance(arr_node.type, ArrayType)
        idx_node: "Exprs" = self.visit(ast.idx, ac)
        codes = (
            arr_node.codes + idx_node.codes + (ac.emit.emitALOAD(arr_node.type.eleType, ac.frame),)
        )
        return Exprs(ast, arr_node.type.eleType, None, codes)

    def visitFieldAccess(self, ast: FieldAccess, ac: Access):
        name = ast.fieldname.name
        obj_node: "TypeDef|Exprs" = self.visit(ast.obj, ac)
        codes: "Tuple[str, ...]"
        if obj_node.is_class is True:
            fname = f"{obj_node.name}.{name}"
            field = obj_node.lookup_member(name, ac.globs)
            codes = (ac.emit.emitGETSTATIC(fname, field.type, ac.frame),)
        else:
            assert isinstance(obj_node.type, ClassType)
            _cls_name = obj_node.type.classname.name
            _cls = ac.globs[_cls_name]
            field = _cls.lookup_member(name, ac.globs)
            fname = f"{_cls_name}.{name}"
            codes = obj_node.codes + (ac.emit.emitGETFIELD(fname, field.type, ac.frame),)
        return Exprs(ast, field.type, None, codes)

    def visitIntLiteral(self, ast: "IntLiteral", ac: Access):
        codes = (ac.emit.emitPUSHICONST(ast.value, ac.frame),)
        return Exprs(ast, int_t, None, codes)

    def visitFloatLiteral(self, ast: FloatLiteral, ac: Access):
        codes = (ac.emit.emitPUSHCONST(str(float(ast.value)), float_t, ac.frame),)
        return Exprs(ast, float_t, None, codes)

    def visitBooleanLiteral(self, ast: BooleanLiteral, ac: Access):
        codes = (ac.emit.emitPUSHICONST(str(ast.value).lower(), ac.frame),)
        return Exprs(ast, bool_t, None, codes)

    def visitStringLiteral(self, ast: StringLiteral, ac: Access):
        codes = (ac.emit.emitPUSHCONST(str(ast.value), str_t, ac.frame),)
        return Exprs(ast, str_t, None, codes)

    def visitArrayLiteral(self, ast: ArrayLiteral, ac: Access):
        from TypeCheck import FlexibleTypeCheck

        elt_chk: "FlexibleTypeCheck" = FlexibleTypeCheck(FlexibleType(dyn=True))
        array_len = len(ast.value)
        buff = [ac.emit.emitPUSHICONST(array_len, ac.frame), NotImplemented]

        for i, e in enumerate(ast.value):
            buff.extend((ac.emit.emitDUP(ac.frame), ac.emit.emitPUSHICONST(i, ac.frame)))
            node: Exprs = self.visit(e, ac)
            buff.extend(node.codes)
            danger: "Any" = ac.globs
            elt_chk.assign_from(node.type, danger)
            buff.append(ac.emit.emitASTORE(node.type, ac.frame))
        ele_type = elt_chk.type.inner
        if isinstance(ele_type, (IntType, FloatType, BoolType)):
            buff[1] = ac.emit.jvm.emitNEWARRAY(ac.emit.getFullType(ele_type))
        elif isinstance(ele_type, (StringType, ArrayType, ClassType, AnyRefType, AnyType)):
            buff[1] = ac.emit.jvm.emitANEWARRAY(ac.emit.getFullType(ele_type))
        else:
            raise Exception("What???")
        return Exprs(ast, ArrayType(array_len, elt_chk.type.inner), None, tuple(buff))

    def visitNullLiteral(self, ast: NullLiteral, ac: Access):
        codes = (ac.emit.emitPUSHCONST("null", NullType(), ac.frame),)
        return Exprs(ast, null_t, None, codes)

    def visitSelfLiteral(self, ast: SelfLiteral, ac: Access):
        assert ac.enclosing
        self_type = ClassType(Id(ac.enclosing))
        codes = (ac.emit.emitREADVAR("this", self_type, 0, ac.frame),)
        return Exprs(ast, self_type, None, codes)

    def visitId(self, ast: Id, ac: Access) -> "Node":
        s = ac.symtable[ast.name]
        if s.is_var is True:
            assert s.local_index is not None
            codes = (ac.emit.emitREADVAR(s.name, s.type, s.local_index, ac.frame),)
            return Exprs(ast, s.type, None, codes)
        else:
            return s
