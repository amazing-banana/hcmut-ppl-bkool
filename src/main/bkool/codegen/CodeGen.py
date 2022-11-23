from typing import List, Tuple

from AST import *
from AdditionalTypes import *
from AstRewrite import AstRewrite
from StmtGen import StmtGen
from CodeGenSymbol import (
    Access,
    EnvTable,
    FuncDef,
    ClassMember,
    ClassTable,
    GlobalClassTable,
    TypeDef,
)

from Frame import Frame
from GlobalSymtabBuilder import GlobalSymtabBuilder
from Visitor import BaseVisitor

__all__ = ["CodeGen"]


class CodeGen(BaseVisitor):
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        f = Frame("top-level", None)
        gl_clses: "tuple[TypeDef,TypeDef]" = self.init()
        init = Access(
            f=f,
            s=True,
            e=None,
            r=None,
            st=EnvTable.FromList(gl_clses),
            gl=GlobalClassTable.FromList(gl_clses),
            sto=False,
            fs=None,
            emit=NotImplemented,
        )
        ac: "Access" = GlobalSymtabBuilder().visit(ast, init)
        r_ast: Program = AstRewrite().visit(ast, ac)
        
        StmtGen(path).visit(r_ast, ac)
        return

    def __init__(self):
        self.libName = "io"

    def init(self):
        io = self.class_factory("io", None, self.IoClass)
        utils = self.class_factory("u", None, self.UtilsClass)
        return io, utils

    def class_factory(self, name, pname, mems) -> TypeDef:
        ms: List[ClassMember]
        ms = [FuncDef(f[0], True, f[1], name) for f in mems]
        symtable = ClassTable.FromList(ms)
        cls = TypeDef(name, pname, symtable)
        return cls

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
        ("arrlen", FuncType([AnyType()], IntType())),
        ("printRef", FuncType([AnyType()], VoidType())),
        ("printLn", FuncType([], VoidType())),
        ("strCmp", FuncType([StringType(), StringType()], BoolType())),
        ("isNotNull", FuncType([AnyType()], BoolType())),
        ("isNull", FuncType([AnyRefType()], BoolType())),
    ]
