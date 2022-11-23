from typing import List, Optional, Tuple

from AST import *
from AdditionalTypes import *
from FirstPassChecker import FirstPassChecker
from SecondPassChecker import SecondPassChecker
from Symbolic import *
from TypeCheker import TypeCheker
from Visitor import BaseVisitor

__all__ = ["StaticCheck"]


class StaticCheck(BaseVisitor):
    IoClass: List[Tuple[str, FuncType]] = [
        ("readInt", FuncType([], IntType())),
        ("writeInt", FuncType([IntType()], VoidType())),
        ("writeIntLn", FuncType([IntType()], VoidType())),
        ("readFloat", FuncType([], FloatType())),
        ("writeFloat", FuncType([FloatType()], VoidType())),
        ("writeFloatLn", FuncType([FloatType()], VoidType())),
        ("readBool", FuncType([], BoolType())),
        ("writeBool", FuncType([BoolType()], VoidType())),
        ("writeBoolLn", FuncType([BoolType()], VoidType())),
        ("readStr", FuncType([], StringType())),
        ("writeStr", FuncType([StringType()], VoidType())),
        ("writeStrLn", FuncType([StringType()], VoidType())),
    ]

    UtilsClass: List[Tuple[str, FuncType]] = [
        ("i2f", FuncType([IntType()], FloatType())),
        ("i2b", FuncType([IntType()], BoolType())),
        ("i2str", FuncType([IntType()], StringType())),
        ("f2i", FuncType([FloatType()], IntType())),
        ("f2b", FuncType([FloatType()], BoolType())),
        ("f2str", FuncType([FloatType()], StringType())),
        ("b2i", FuncType([BoolType()], IntType())),
        ("b2f", FuncType([BoolType()], FloatType())),
        ("b2str", FuncType([BoolType()], StringType())),
        ("str2i", FuncType([StringType()], IntType())),
        ("str2f", FuncType([StringType()], FloatType())),
        ("str2b", FuncType([StringType()], BoolType())),
        ("strlen", FuncType([StringType()], IntType())),
        ("arrlen", FuncType([AnyRefType()], IntType())),
        # Negative for non-array type
        ("printRef", FuncType([AnyRefType()], VoidType())),
        ("printLn", FuncType([], VoidType())),
        ("strCmp", FuncType([StringType(), StringType()], BoolType())),
        ("isNull", FuncType([AnyRefType()], BoolType())),
        ("isNotNull", FuncType([AnyRefType()], BoolType())),
    ]
    typechk = TypeCheker()

    def __init__(self, ast: Program):
        self.ast: Program = ast

    def check(self, _: Optional[Scoping] = None) -> Scoping:
        io = self.io_class()
        utils = self.utils_class()
        syms = GlobalClassTable({"io": io, "u": utils})
        b = Scoping(
            stat=True,
            ecls=None,
            rtype=None,
            syms=syms,
            globs=syms,
            parent=None,
        )
        b0 = FirstPassChecker(self.ast).check(b)
        b1 = SecondPassChecker(self.ast).check(b0)
        return b1  # self.visit(self.ast, b)

    def io_class(self) -> TypeDef:
        name = "io"
        parent = None
        ms: List[ClassMember]
        fc = self.typechk.visit
        ms = [FuncDef(f[0], True, f[1], fc(f[1], None), "io") for f in self.IoClass]
        symtable = ClassTable.FromList(ms)
        io_class_ = TypeDef(name, parent, symtable)
        return io_class_

    def utils_class(self) -> TypeDef:
        name = "u"
        parent = None
        ms: List[ClassMember]
        fc = self.typechk.visit
        ms = [FuncDef(f[0], True, f[1], fc(f[1], None), "u") for f in self.UtilsClass]
        symtable = ClassTable.FromList(ms)
        utils_class_ = TypeDef(name, parent, symtable)
        return utils_class_

    ...
