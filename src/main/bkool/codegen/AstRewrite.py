import sys

sys.path.append("./src/main/bkool/utils/")

from functools import reduce
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional as Opt,
    Tuple,
    Union,
    List,
)

from AST import *
from Visitor import BaseVisitor
from operator import add as add_f, mul as mul_f
from AdditionalTypes import ArraysOfDefault

if TYPE_CHECKING:
    Primitive = Union[int, float, str, bool]

PrimitiveLit = (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)


def or_f(a, e):
    return a or e


def and_f(a, e):
    return a and e


def fold(exprs: Tuple[Expr, ...], op: str) -> Any:
    if op == "^":
        return fold_string(exprs)
    op_dict = {"+": add_f, "*": mul_f, "||": or_f, "&&": and_f}
    func = op_dict.get(op)
    if func is None:
        raise Exception(f"Unknown {op} in fold")
    else:
        return fold_expr(exprs, func)


def fold_expr(
        exprs: Tuple[Expr, ...], func: "Callable[[Any,Any], Any]"
) -> Tuple[Expr, ...]:
    buff: List[Any] = []
    res: List[Expr] = []
    Cls = None
    for e in exprs:
        if isinstance(e, PrimitiveLit):
            Cls = aggregate_type(Cls, type(e))
            if skipable(func, e.value, buff):
                continue
            buff.append(e.value)
        else:
            if len(buff) > 0:
                assert Cls
                res.append(Cls(reduce(func, buff)))
                buff = []
            res.append(e)
    if len(buff) > 0:
        assert Cls
        return *res, Cls(reduce(func, buff))
    else:
        return tuple(res)


def skipable(f, v, b) -> bool:
    return (f is add_f and v == 0) or (
            f is mul_f and ((v == 1) or (v == 0 and (0 in b)))
    )


def fold_string(exprs: Tuple[Expr, ...]) -> Tuple[Expr, ...]:
    buff = []
    res: List[Expr] = []
    for e in exprs:
        if isinstance(e, StringLiteral):
            if e.value != '""':
                buff.append(e.value[1:-1])
        else:
            if len(buff) > 0:
                res.append(StringLiteral(f'"{"".join(buff)}"'))
                buff = []
            res.append(e)
    if len(buff) > 0:
        res.append(StringLiteral(f'"{"".join(buff)}"'))
    return tuple(res)


def to_expr(folded: Tuple[Expr, ...], op: str) -> "Expr":
    # folded = ( 1 ; (* 2 (* 3 1)) ; (-4) ), op = "+"
    # -> + {+ 1 [* 2 (* 3 1)]} (-4)
    #    (1) -> (1)
    # if len(folded) < 2 -> folded[0] else reduce(...)

    return reduce(lambda a, e: BinaryOp(op, a, e), folded[1:], folded[0])


def flatten_unop(ast: Expr, op: str, count: int = 0):
    if not isinstance(ast, UnaryOp) or ast.op != op:
        return ast, count
    else:
        return flatten_unop(ast.body, op, count + 1)


def flatten_add_expr(ast: Expr, op: str) -> Tuple[Expr, ...]:
    # 1 + ((2 * (3 * 1)) + (-4))
    # -> 1, ((2 * (3 * 1)), -4
    if not isinstance(ast, BinaryOp) or ast.op != op:
        return (ast,)
    else:
        return flatten_add_expr(ast.left, op) + flatten_add_expr(ast.right, op)


def eval_unexpr(op: str, body: "Primitive"):
    pyop = "not" if op == "!" else op
    try:
        return eval(f"{pyop} {body}")
    except Exception:
        return None


def eval_binexpr(op: str, left: "Primitive", right: "Primitive"):
    pyop = "and" if op == "&&" else "or" if op == "||" else op
    try:
        return eval(f"{left} {pyop} {right}")
    except Exception:
        return None


def aggregate_type(left: Any, right: Any, op: "Opt[str]" = None) -> Any:
    if left is None:
        return right
    elif op in ("<", ">", "<=", ">=", "==", "!="):
        return BooleanLiteral
    elif op == "/":
        return FloatLiteral
    else:
        return FloatLiteral if FloatLiteral in (left, right) else left


class AstRewrite(BaseVisitor):
    # Basic Operands
    def visitIntLiteral(self, ast: IntLiteral, o):
        return ast

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return ast

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return ast

    def visitStringLiteral(self, ast: StringLiteral, o):
        return ast

    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        return ast

    def visitNullLiteral(self, ast: NullLiteral, o):
        return ast

    def visitSelfLiteral(self, ast: SelfLiteral, o):
        return ast

    def visitId(self, ast: Id, o):
        return ast

    # Complex Expr
    def visitBinaryOp(self, ast: BinaryOp, o):
        if ast.op in ("+", "*", "^", "||", "&&"):
            original = flatten_add_expr(ast, ast.op)
            rewrite = tuple(self.visit(e, o) for e in original)
            folded = fold(rewrite, ast.op)
            return to_expr(folded, ast.op)
        else:
            left = self.visit(ast.left, o)
            right = self.visit(ast.right, o)
            if isinstance(left, PrimitiveLit) and isinstance(right, PrimitiveLit):
                val = eval_binexpr(ast.op, left.value, right.value)
                if val is not None:
                    Cls = aggregate_type(type(left), type(right), ast.op)
                    return Cls(val)

        return BinaryOp(ast.op, left, right)

    def visitUnaryOp(self, ast: UnaryOp, o):
        expr, dup = flatten_unop(ast, ast.op)
        body = self.visit(expr, o)
        if ast.op == "+":
            return body
        if isinstance(body, PrimitiveLit):
            val = eval_unexpr(ast.op, body.value) if dup % 2 != 0 else body.value
            if val is not None:
                body.value = val  # type: ignore
                return body
        if ast.op == "!":  # what about "-" ?
            if dup % 2 == 0:
                return body
            else:
                ast.body = body
        return ast

    def visitCallExpr(self, ast: CallExpr, o):
        obj = self.visit(ast.obj, o)
        args = [self.visit(a, o) for a in ast.param]
        return CallExpr(obj, ast.method, args)

    def visitNewExpr(self, ast: NewExpr, o):
        args = [self.visit(a, o) for a in ast.param]
        return NewExpr(ast.classname, args)

    def visitArrayCell(self, ast: ArrayCell, o):
        arr = self.visit(ast.arr, o)
        idx = self.visit(ast.idx, o)
        return ArrayCell(arr, idx)

    def visitFieldAccess(self, ast: FieldAccess, o):
        obj = self.visit(ast.obj, o)
        return FieldAccess(obj, ast.fieldname)

    # Top-level

    def visitProgram(self, ast: Program, o):
        [self.visit(d, o) for d in ast.decl]
        return ast

    def visitClassDecl(self, ast: ClassDecl, o):
        [self.visit(m, o) for m in ast.memlist]
        return ast

    def visitMethodDecl(self, ast: MethodDecl, o):
        [self.visit(p, o) for p in ast.param]
        self.visit(ast.body, o)
        return ast

    def visitAttributeDecl(self, ast: AttributeDecl, o):
        self.visit(ast.decl, o)
        return ast

    # Stmts Contain expr
    def visitVarDecl(self, ast: VarDecl, o):
        if ast.varInit:
            ast.varInit = self.visit(ast.varInit, o)
        elif isinstance(ast.varType, ArrayType):
            ast.varInit = ArraysOfDefault(ast.varType)
        return ast

    def visitConstDecl(self, ast: ConstDecl, o):
        ast.value = self.visit(ast.value, o) if ast.value else None
        return ast

    def visitIf(self, ast: If, o):
        ast.expr = self.visit(ast.expr, o)
        self.visit(ast.thenStmt, o)
        self.visit(ast.elseStmt, o) if ast.elseStmt else None
        return ast

    def visitFor(self, ast: For, o):
        ast.expr1 = self.visit(ast.expr1, o)
        ast.expr2 = self.visit(ast.expr2, o)
        self.visit(ast.loop, o)
        return ast

    def visitReturn(self, ast: Return, o):
        ast.expr = self.visit(ast.expr, o)
        return ast

    def visitAssign(self, ast: Assign, o):
        ast.lhs = self.visit(ast.lhs, o)
        ast.exp = self.visit(ast.exp, o)
        return ast

    def visitCallStmt(self, ast: CallStmt, o):
        ast.obj = self.visit(ast.obj, o)
        ast.param = [self.visit(a, o) for a in ast.param]
        return ast

    # Other Stmts

    def visitBlock(self, ast: Block, o):
        [self.visit(d, o) for d in ast.decl]
        [self.visit(stmt, o) for stmt in ast.stmt]
        return ast

    def visitContinue(self, ast: Continue, o):
        return ast

    def visitBreak(self, ast: Break, o):
        return ast

    # Other stuff

    def visitStatic(self, ast: Static, o):
        return ast

    def visitInstance(self, ast: Instance, o):
        return ast

    def visitIntType(self, ast: IntType, o):
        return ast

    def visitFloatType(self, ast: FloatType, o):
        return ast

    def visitBoolType(self, ast: BoolType, o):
        return ast

    def visitStringType(self, ast: StringType, o):
        return ast

    def visitVoidType(self, ast: VoidType, o):
        return ast

    def visitArrayType(self, ast: ArrayType, o):
        return ast

    def visitClassType(self, ast: ClassType, o):
        return ast


def test():
    base = BooleanLiteral(True)
    _12 = BinaryOp("+", IntLiteral(1), IntLiteral(2))
    _12a = BinaryOp("+", _12, Id("a"))
    _34 = BinaryOp("+", IntLiteral(3), IntLiteral(4))
    _12a34 = BinaryOp("+", _12a, _34)
    uuuunop = UnaryOp("!", UnaryOp("!", UnaryOp("!", UnaryOp("-", UnaryOp("-", base)))))
    biop = BinaryOp("+", Id("a"), uuuunop)
    ru1 = AstRewrite().visit(uuuunop, None)
    ru2 = AstRewrite().visit(_12a34, None)
    ru2 = AstRewrite().visit(_12a34, None)

    prog = Program(
        [
            ClassDecl(
                Id("A"),
                [
                    MethodDecl(
                        Instance(),
                        Id("<init>"),
                        [VarDecl(Id("ha"), IntType(), None)],
                        None,
                        Block([], []),
                    )
                ],
                Id("BKoolClass"),
            ),
            ClassDecl(
                Id("B"),
                [
                    MethodDecl(
                        Instance(),
                        Id("<init>"),
                        [VarDecl(Id("ha"), IntType(), None)],
                        None,
                        Block([], []),
                    )
                ],
                Id("A"),
            ),
            ClassDecl(
                Id("BKoolClass"),
                [
                    MethodDecl(
                        Static(),
                        Id("main"),
                        [VarDecl(Id("args"), ArrayType(0, StringType()), None)],
                        VoidType(),
                        Block(
                            [],
                            [
                                CallStmt(
                                    Id("io"),
                                    Id("writeStrLn"),
                                    [StringLiteral("HAHA Haha")],
                                )
                            ],
                        ),
                    )
                ],
                None,
            ),
        ]
    )
    rprog = AstRewrite().visit(prog, None)
    print(rprog)


def prog_test():
    prog = Program(
        [
            ClassDecl(
                Id("A"),
                [
                    MethodDecl(
                        Instance(),
                        Id("<init>"),
                        [VarDecl(Id("ha"), IntType(), None)],
                        None,
                        Block([], []),
                    )
                ],
                Id("BKoolClass"),
            ),
            ClassDecl(
                Id("B"),
                [
                    MethodDecl(
                        Instance(),
                        Id("<init>"),
                        [VarDecl(Id("ha"), IntType(), None)],
                        None,
                        Block([], []),
                    )
                ],
                Id("A"),
            ),
            ClassDecl(
                Id("BKoolClass"),
                [
                    MethodDecl(
                        Static(),
                        Id("main"),
                        [VarDecl(Id("args"), ArrayType(0, StringType()), None)],
                        VoidType(),
                        Block(
                            [],
                            [
                                CallStmt(
                                    Id("io"),
                                    Id("writeStrLn"),
                                    [
                                        BinaryOp(
                                            "^",
                                            StringLiteral("HAHA Haha "),
                                            StringLiteral("Hehe"),
                                        )
                                    ],
                                )
                            ],
                        ),
                    )
                ],
                None,
            ),
        ]
    )

    rprog = AstRewrite().visit(prog, None)
    expr = BinaryOp("^", StringLiteral("HAHA Haha "), StringLiteral("Hehe"))
    rexpr = AstRewrite().visit(expr, None)
    print(rexpr.value == "HAHA Haha Hehe")


if __name__ == "__main__":
    prog_test()
