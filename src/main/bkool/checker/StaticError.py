# update: 16/07/2018
from abc import ABC
from dataclasses import dataclass
from typing import Optional, Union

from AST import *

__all__ = [
    "Kind",
    "Class",
    "Method",
    "SpecialMethod",
    "Attribute",
    "Parameter",
    "Constant",
    "Variable",
    "Identifier",
    "StaticError",
    "Undeclared",
    "UndeclaredIdentifier",
    "UndeclaredClass",
    "UndeclaredAttribute",
    "UndeclaredMethod",
    "Redeclared",
    "TypeMismatchInExpression",
    "TypeMismatchInStatement",
    "CannotAssignToConstant",
    "TypeMismatchInConstant",
    "NotConstantExpression",
    "MustInLoop",
    "IllegalConstantExpression",
    "IllegalArrayLiteral",
    "IllegalMemberAccess",
    "FunctionNotReturn",
    "BreakNotInLoop",
    "ContinueNotInLoop",
    "NoEntryPoint",
    "UnreachableStatement",
    "UnreachableFunction",
]


class Kind(ABC):
    pass


class Class(Kind):
    def __str__(self):
        return "Class"


class Method(Kind):
    def __str__(self):
        return "Method"


class SpecialMethod(Kind):
    def __str__(self):
        return "Special Method"


class Attribute(Kind):
    def __str__(self):
        return "Attribute"


class Parameter(Kind):
    def __str__(self):
        return "Parameter"


class Constant(Kind):
    def __str__(self):
        return "Constant"


class Variable(Kind):
    def __str__(self):
        return "Variable"


class Identifier(Kind):
    def __str__(self):
        return "Identifier"


class StaticError(Exception):
    pass


@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # op of identifier

    def __init__(self, k: Kind, n: str):
        self.k = k
        self.n = n

    def __str__(self):
        return "Undeclared " + str(self.k) + ": " + self.n


class UndeclaredIdentifier(StaticError):
    n: str  # op of identifier

    def __init__(self, n: str):
        self.n = n

    def __str__(self):
        return "Undeclared Identifier: " + self.n


class UndeclaredClass(StaticError):
    n: str  # op of identifier

    def __init__(self, n: str):
        self.n = n

    def __str__(self):
        return "Undeclared Class: " + self.n


class UndeclaredAttribute(StaticError):
    n: str  # op of identifier

    def __init__(self, n: str):
        self.n = n

    def __str__(self):
        return "Undeclared Attribute: " + self.n


class UndeclaredMethod(StaticError):
    n: str  # op of identifier

    def __init__(self, n: str):
        self.n = n

    def __str__(self):
        return "Undeclared Method: " + self.n


@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str  # op of identifier

    def __init__(self, k: Kind, n: str):
        self.k = k
        self.n = n

    def __str__(self):
        return "Redeclared " + str(self.k) + ": " + self.n


@dataclass
class TypeMismatchInExpression(StaticError):
    """
    exp: AST.Expr
    Array: elements must be same type
    Binary/Unary: must be correct type
    Call:
    \t Invoker must be class type
    \t return type must be non-void
    \t Param must be right type
    Member Access: accessor must be class type
    """

    exp: Expr

    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.exp)


@dataclass
class TypeMismatchInStatement(StaticError):
    """
    :param stmt: Statement
    If: condition expr must be bool\n
    For: Iterator must be scala type\n
    Assign:
    \t lhs must not be void type
    \t rhs must be same type as lhs or can coerece to lhs
    Call:
    \t Invoker must be class type
    \t method must be void type.
    \t param must be right type
    Return: expr must be able to coerce into return type
    """

    stmt: Stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


@dataclass
class CannotAssignToConstant(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Cannot Assign To Constant: " + str(self.stmt)


@dataclass
class TypeMismatchInConstant(StaticError):
    constdecl: ConstDecl

    def __str__(self):
        return "Type Mismatch In Constant Declaration: " + str(self.constdecl)


@dataclass
class NotConstantExpression(StaticError):
    expr: Expr

    def __str__(self):
        return "Not Constant Expression: " + str(self.expr)


@dataclass
class MustInLoop(StaticError):
    stmt: Stmt

    def __str__(self):
        return str(self.stmt) + " Not In Loop"


@dataclass
class IllegalConstantExpression(StaticError):
    expr: Optional[Expr]

    def __str__(self):
        return "Illegal Constant Expression: " + str(self.expr)


@dataclass
class IllegalArrayLiteral(StaticError):
    arr: ArrayLiteral

    def __str__(self):
        return "Illegal Array Literal: " + str(self.arr)


@dataclass
class IllegalMemberAccess(StaticError):
    expr: Union[CallExpr, CallStmt, FieldAccess]

    def __str__(self):
        return "Illegal Member Access: " + str(self.expr)


# Not use #
class FunctionNotReturn(StaticError):
    """m is a string that is the op of the function"""

    def __init__(self, m):
        self.m = m

    def __str__(self):
        return "Function " + self.m + " Not Return "


class BreakNotInLoop(StaticError):
    def __str__(self):
        return "Break Not In Loop"


class ContinueNotInLoop(StaticError):
    def __str__(self):
        return "Continue Not In Loop"


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"


class UnreachableStatement(StaticError):
    """stmt is AST.Stmt"""

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Unreachable statement: " + str(self.stmt)


class UnreachableFunction(StaticError):
    """m is a string that is the op of the unreachable function"""

    def __init__(self, m):
        self.m = m

    def __str__(self):
        return "Unreachable function: " + self.m
