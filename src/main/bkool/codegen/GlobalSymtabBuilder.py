from typing import TYPE_CHECKING, List

from AST import *
from AdditionalTypes import FuncType
from CodeGenSymbol import (
    TypeDef,
    FuncDef,
    LocalVar,
    LocalConst,
    VarDefGeneric,
    ClassMember,
    ClassTable,
)
from Visitor import BaseVisitor

if TYPE_CHECKING:
    from CodeGenSymbol import Access, LocalDefType

__all__ = ["GlobalSymtabBuilder"]
Bogus = NotImplemented


class GlobalSymtabBuilder(BaseVisitor):
    def visitProgram(self, ast: Program, c: "Access"):
        classes: List[TypeDef] = [self.visit(d, c) for d in ast.decl]
        c.globs.update((e.name, e) for e in classes)
        c.symtable.update((e.name, e) for e in classes)
        return c

    def visitClassDecl(self, ast: ClassDecl, c: "Access"):
        name = ast.classname.name
        pname = ast.parentname.name if ast.parentname else None
        mems: List[ClassMember]
        c.enclosing = name
        mems = [self.visit(m, c) for m in ast.memlist]
        c.enclosing = None
        tabl = ClassTable.FromList(mems)
        return TypeDef(name, pname, tabl)

    def visitAttributeDecl(self, ast: AttributeDecl, c: "Access"):
        assert c.enclosing
        contg_cls = c.enclosing
        v: "LocalDefType" = self.visit(ast.decl, c)
        static = isinstance(ast.kind, Static)
        return v.to_attr(static, contg_cls)

    def visitVarDecl(self, ast: VarDecl, c: "Access"):
        name = ast.variable.name
        type_ = ast.varType
        return LocalVar(name, type_, NotImplemented)

    def visitConstDecl(self, ast: ConstDecl, c: "Access"):
        assert ast.value
        name = ast.constant.name
        type_ = ast.constType
        ast_value = ast.value
        return LocalConst(name, type_, NotImplemented, ast_value)

    def visitMethodDecl(self, ast: MethodDecl, c: "Access"):
        assert c.enclosing
        name = ast.name.name
        static = isinstance(ast.kind, Static)
        params: List[VarDefGeneric] = [self.visit(p, c) for p in ast.param]
        params_t = [p.type for p in params]
        return_type = ast.returnType if ast.returnType else VoidType()
        ftype = FuncType(params_t, return_type)
        return FuncDef(name, static, ftype, c.enclosing)
