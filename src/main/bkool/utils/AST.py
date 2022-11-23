from abc import ABC, ABCMeta
from dataclasses import dataclass
from typing import Any, Union, List, Optional

from Visitor import Visitor

__all__ = [
    "AST",
    "Stmt",
    "Expr",
    "LHS",
    "Type",
    "MemDecl",
    "Id",
    "BinaryOp",
    "UnaryOp",
    "CallExpr",
    "NewExpr",
    "ArrayCell",
    "FieldAccess",
    "Literal",
    "IntLiteral",
    "FloatLiteral",
    "StringLiteral",
    "BooleanLiteral",
    "NullLiteral",
    "SelfLiteral",
    "ArrayLiteral",
    "Decl",
    "StoreDecl",
    "Assign",
    "If",
    "For",
    "Break",
    "Continue",
    "Return",
    "CallStmt",
    "VarDecl",
    "Block",
    "ConstDecl",
    "ClassDecl",
    "SIKind",
    "Instance",
    "Static",
    "MethodDecl",
    "AttributeDecl",
    "IntType",
    "FloatType",
    "BoolType",
    "StringType",
    "ArrayType",
    "ClassType",
    "VoidType",
    "Program",
]


class AST(ABC):
    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def accept(self, v: Visitor, param: Any) -> Any:
        method_name = "visit{}".format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class Type(AST):
    __metaclass__ = ABCMeta
    pass


class MemDecl(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Id(LHS):
    name: str

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "Id(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitId(self, param)


# used for binary expression
@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "BinaryOp(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitBinaryOp(self, param)


# used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op: str
    body: Expr

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "UnaryOp(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitUnaryOp(self, param)


@dataclass
class CallExpr(Expr):
    obj: Expr
    method: Id
    param: List[Expr]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "CallExpr(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "CallExpr("
            + str(self.obj)
            + ","
            + str(self.method)
            + ",["
            + ",".join(str(i) for i in self.param)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitCallExpr(self, param)


@dataclass
class NewExpr(Expr):
    classname: Id
    param: List[Expr]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "NewExpr(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "NewExpr("
            + str(self.classname)
            + ",["
            + ",".join(str(i) for i in self.param)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitNewExpr(self, param)


@dataclass
class ArrayCell(LHS):
    arr: Expr
    idx: Expr

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "ArrayCell(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitArrayCell(self, param)


@dataclass
class FieldAccess(LHS):
    obj: Expr
    fieldname: Id

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "FieldAccess(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "FieldAccess(" + str(self.obj) + "," + str(self.fieldname) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitFieldAccess(self, param)


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass


@dataclass
class IntLiteral(Literal):
    value: int

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "IntLiteral(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "IntLit(" + str(self.value) + ")"

    def accept(self, v: Visitor, param):
        return v.visitIntLiteral(self, param)


@dataclass
class FloatLiteral(Literal):
    value: float

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "FloatLiteral(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "FloatLit(" + str(self.value) + ")"

    def accept(self, v: Visitor, param):
        return v.visitFloatLiteral(self, param)


@dataclass
class StringLiteral(Literal):
    value: str

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "StringLiteral(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "StringLit(" + self.value + ")"

    def accept(self, v: Visitor, param):
        return v.visitStringLiteral(self, param)


@dataclass
class BooleanLiteral(Literal):
    value: bool

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "BooleanLiteral(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "BooleanLit(" + str(self.value) + ")"

    def accept(self, v: Visitor, param):
        return v.visitBooleanLiteral(self, param)


class NullLiteral(Literal):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "NullLiteral()"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitNullLiteral(self, param)


class SelfLiteral(Literal):
    def __repr__(self):
        return "SelfLiteral()"

    def __str__(self):
        return "Self()"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitSelfLiteral(self, param)


@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "ArrayLiteral(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "[" + ",".join(str(i) for i in self.value) + "]"

    def accept(self, v: Visitor, param):
        return v.visitArrayLiteral(self, param)


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class StoreDecl(Decl):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Assign(Stmt):
    lhs: Expr
    exp: Expr

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "Assign(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + "," + str(self.exp) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitAssign(self, param)


@dataclass
class If(Stmt):
    expr: Expr
    thenStmt: Stmt
    elseStmt: Optional[Stmt] = None  # None if there is no else branch

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "If(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "If("
            + str(self.expr)
            + ","
            + str(self.thenStmt)
            + (("," + str(self.elseStmt)) if self.elseStmt else "")
            + ")"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitIf(self, param)


@dataclass
class For(Stmt):
    id: Id
    expr1: Expr
    expr2: Expr
    up: bool  # True => increase; False => decrease
    loop: Stmt

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "For(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "For("
            + str(self.id)
            + ","
            + str(self.expr1)
            + ","
            + str(self.expr2)
            + ","
            + str(self.up)
            + ","
            + str(self.loop)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitFor(self, param)


class Break(Stmt):
    def __repr__(self):
        return "Break()"

    def __str__(self):
        return "Break"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitBreak(self, param)


class Continue(Stmt):
    def __repr__(self):
        return "Continue()"

    def __str__(self):
        return "Continue"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitContinue(self, param)


@dataclass
class Return(Stmt):
    expr: Expr

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "Return(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return "Return(" + str(self.expr) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitReturn(self, param)


@dataclass
class CallStmt(Stmt):
    obj: Expr
    method: Id
    param: List[Expr]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "CallStmt(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "Call("
            + str(self.obj)
            + ","
            + str(self.method)
            + ",["
            + ",".join(str(i) for i in self.param)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitCallStmt(self, param)


# used for local variable or parameter declaration
@dataclass
class VarDecl(StoreDecl):
    variable: Id
    varType: Type
    varInit: Optional[Expr] = None  # None if there is no initial

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "VarDecl(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "VarDecl("
            + str(self.variable)
            + ","
            + str(self.varType)
            + ("," + str(self.varInit) if self.varInit else "")
            + ")"
        )

    def toParam(self):
        return "param(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitVarDecl(self, param)


@dataclass
class Block(Stmt):
    decl: List[StoreDecl]
    stmt: List[Stmt]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "Block(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "Block(["
            + ",".join(str(i) for i in self.decl)
            + "],["
            + ",".join(str(i) for i in self.stmt)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitBlock(self, param)


# used for local constant declaration
@dataclass
class ConstDecl(StoreDecl):
    constant: Id
    constType: Type
    value: Optional[Expr]

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "ConstDecl(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "ConstDecl("
            + str(self.constant)
            + ","
            + str(self.constType)
            + ","
            + str(self.value)
            + ")"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitConstDecl(self, param)


# used for a class declaration
@dataclass
class ClassDecl(Decl):
    classname: Id
    memlist: List[MemDecl]
    parentname: Optional[Id] = None  # None if there is no parent

    # parentname: Id = None  # None if there is no parent

    def __repr__(self):
        attr_name = list(
            map(
                lambda e: self.__getattribute__(e),
                list(self.__dataclass_fields__.keys()),
            )
        )
        return "ClassDecl(" + ",".join(repr(e) for e in attr_name) + ")"

    def __str__(self):
        return (
            "ClassDecl("
            + str(self.classname)
            + (("," + str(self.parentname)) if self.parentname else "")
            + ",["
            + ",".join(str(i) for i in self.memlist)
            + "])"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitClassDecl(self, param)


class SIKind(AST):
    __metaclass__ = ABCMeta


# used for instance member
class Instance(SIKind):
    def __repr__(self):
        return "Instance()"

    def __str__(self):
        return "Instance"

    def accept(self, v: Visitor, param):
        return v.visitInstance(self, param)


# used for s member
class Static(SIKind):
    def __repr__(self):
        return "Static()"

    def __str__(self):
        return "Static"

    def accept(self, v: Visitor, param):
        return v.visitStatic(self, param)


# used for a normal or special method declaration.
# In the case of special method declaration,the op will be Id("<init>")
# and the return type is None.
# In the case of normal method declaration, the op and the return type are from the declaration.
@dataclass
class MethodDecl(MemDecl):
    kind: SIKind
    name: Id
    param: List[VarDecl]
    returnType: Optional[Type]  # None for constructor
    body: Block

    def __repr__(self):
        return (
            "MethodDecl("
            + repr(self.kind)
            + ","
            + repr(self.name)
            + ","
            + repr(self.param)
            + ","
            + repr(self.returnType)
            + ","
            + repr(self.body)
            + ")"
        )

    def __str__(self):
        return (
            "MethodDecl("
            + str(self.name)
            + ","
            + str(self.kind)
            + ",["
            + ",".join(i.toParam() for i in self.param)
            + "],"
            + ((str(self.returnType) + ",") if self.returnType else "")
            + str(self.body)
            + ")"
        )

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitMethodDecl(self, param)


# used for mutable (variable) or immutable (constant) declaration
@dataclass
class AttributeDecl(MemDecl):
    kind: SIKind  # Instance or Static
    decl: "Union[VarDecl,ConstDecl]"  # VarDecl for mutable or ConstDecl for immutable

    def __repr__(self):
        return "AttributeDecl(" + repr(self.kind) + "," + repr(self.decl) + ")"

    def __str__(self):
        return "AttributeDecl(" + str(self.kind) + "," + str(self.decl) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitAttributeDecl(self, param)


class IntType(Type):
    def __repr__(self):
        return str(self) + "()"

    def __str__(self):
        return "IntType"

    def accept(self, v: Visitor, param):
        return v.visitIntType(self, param)


class FloatType(Type):
    def __repr__(self):
        return str(self) + "()"

    def __str__(self):
        return "FloatType"

    def accept(self, v: Visitor, param):
        return v.visitFloatType(self, param)


class BoolType(Type):
    def __repr__(self):
        return str(self) + "()"

    def __str__(self):
        return "BoolType"

    def accept(self, v: Visitor, param):
        return v.visitBoolType(self, param)


class StringType(Type):
    def __repr__(self):
        return str(self) + "()"

    def __str__(self):
        return "StringType"

    def accept(self, v: Visitor, param):
        return v.visitStringType(self, param)


@dataclass
class ArrayType(Type):
    size: int
    eleType: Type

    def __repr__(self):
        return "ArrayType(" + repr(self.size) + "," + repr(self.eleType) + ")"

    def __str__(self):
        return "ArrayType(" + str(self.size) + "," + str(self.eleType) + ")"

    def __eq__(self, other: Any):
        return self.size == other.size and self.eleType == other.eleType

    def accept(self, v: Visitor, param):
        return v.visitArrayType(self, param)


@dataclass
class ClassType(Type):
    classname: Id

    def __repr__(self):
        return "ClassType(" + repr(self.classname) + ")"

    def __str__(self):
        return "ClassType(" + str(self.classname) + ")"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitClassType(self, param)


class VoidType(Type):
    def __repr__(self):
        return str(self) + "()"

    def __str__(self):
        return "VoidType"

    def accept(self, v: Visitor, param):
        return v.visitVoidType(self, param)


# used for whole program
@dataclass
class Program(AST):
    decl: List[ClassDecl]

    def __repr__(self):
        return "Program([" + ",".join(repr(i) for i in self.decl) + "])"

    def __str__(self):
        return "Program([" + ",".join(str(i) for i in self.decl) + "])"

    def accept(self, v: Visitor, param: Any) -> Any:
        return v.visitProgram(self, param)
