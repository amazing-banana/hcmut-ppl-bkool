from typing import Any as any_t

from AST import *
from AdditionalTypes import FuncType, NullType, AnyType, AnyRefType, FlexibleType
from TypeCheck import (
    BkoolTypeCheck,
    IntTypeCheck,
    FloatTypeCheck,
    BoolTypeCheck,
    StringTypeCheck,
    VoidTypeCheck,
    ArrayTypeCheck,
    ClassTypeCheck,
    NullTypeCheck,
    FuncTypeCheck,
    AnyTypeCheck,
    AnyRefTypeCheck,
    FlexibleTypeCheck,
    Int, Float, Bool, String, Void, Any, AnyRef, Null
)
from Visitor import BaseVisitor

__all__ = ["TypeCheker", "Int", "Float", "Bool", "String", "Void", "Any", "AnyRef", "Null"]


class TypeCheker(BaseVisitor):
    def check(self, ast: Type, may_unused: any_t = None) -> "BkoolTypeCheck[Type]":
        return self.visit(ast, may_unused)

    @staticmethod
    def visitAnyRefType(ast: "AnyRefType", b=None) -> "AnyRefTypeCheck":
        return AnyRef

    @staticmethod
    def visitAnyType(ast: "AnyType", b=None) -> "AnyTypeCheck":
        return Any

    @staticmethod
    def visitNullType(ast: "NullType", b=None) -> "NullTypeCheck":
        return Null

    @staticmethod
    def visitFuncType(ast: "FuncType", b=None) -> "FuncTypeCheck":
        return FuncTypeCheck(ast)

    @staticmethod
    def visitFlexibleType(ast: "FlexibleType", b=None) -> "FlexibleTypeCheck":
        return FlexibleTypeCheck(ast)

    def visitArrayType(self, ast: "ArrayType", b=None) -> "ArrayTypeCheck":
        return ArrayTypeCheck(ast)

    def visitClassType(self, ast: "ClassType", b=None) -> "ClassTypeCheck":
        return ClassTypeCheck(ast)

    def visitIntType(self, ast: "IntType", b=None) -> "IntTypeCheck":
        return Int

    def visitFloatType(self, ast: "FloatType", b=None) -> "FloatTypeCheck":
        return Float

    def visitBoolType(self, ast: "BoolType", b=None) -> "BoolTypeCheck":
        return Bool

    def visitStringType(self, ast: "StringType", b=None) -> "StringTypeCheck":
        return String

    def visitVoidType(self, ast: "VoidType", b=None) -> "VoidTypeCheck":
        return Void
