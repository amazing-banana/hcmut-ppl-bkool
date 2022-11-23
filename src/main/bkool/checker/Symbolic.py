from dataclasses import dataclass  # beware! does not work for py < 3.7
from functools import lru_cache
from typing import TYPE_CHECKING, Union, Tuple, Optional, overload, Generic, Dict, TypeVar, cast

from AST import *
from AdditionalTypes import *
from ReachableBlock import ControlBlock

if TYPE_CHECKING:
    from ExprChecker import ExprChecker
    from typing import (
        Literal as PyLit,
        Generator,
        Any as any_t,
        Final,
        Callable,
        NoReturn,
        List,
        Sequence,
        Type as TypeOf,
    )
    from TypeCheck import *
    from typing_extensions import reveal_type

__all__ = [
    "Node",
    "Symbol",
    "TypeDef",
    "FuncDef",
    "VarDef",
    "LocalVar",
    "LocalConst",
    "ExprNode",
    "ClassMember",
    "TrueSymbol",
    "SymbolTable",
    "ClassTable",
    "GlobalClassTable",
    "Scoping",
]


def _get_typecheck(t: "Type", any: "any_t" = None) -> "any_t":
    @lru_cache(maxsize=2)
    def get_visitor():
        import TypeCheker as m  # avoid circular import

        return m.TypeCheker()

    return get_visitor().check(t, any)


def equal(_a: "Tuple[str, str]", _b: "Tuple[str, str]") -> "bool":
    # Same class, diff kind, same name? not possible
    return _a[0] == _b[0] and _a[1] is _b[1]


Symbol = Union["TypeDef", "FuncDef", "VarDef"]
Node = Union["Symbol", "ExprNode"]


@dataclass
class TypeDef:
    __slots__ = (
        "name",
        "is_class",
        "is_func",
        "is_var",
        "is_expr",
        "parent",
        "symtable",
    )

    def __init__(self, name: "str", parent: "Optional[str]", syms: "ClassTable") -> "None":
        self.name: "Final[str]" = name

        self.is_class: "Final[PyLit[True]]" = True
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[False]]" = False

        self.parent: Final[Optional[str]] = parent
        self.symtable: Final[ClassTable] = syms

    def lookup_member(self, name, globs, thrower, static=False):
        # type: (str, GlobalClassTable,Callable[[bool,str],NoReturn],bool) -> 'ClassMember'
        m = self.symtable.get(name)
        pname = self.parent
        if m is None and static:
            thrower(True, name)
        while m is None:
            if pname is None:
                thrower(True, name)
            pdef: "Optional[TypeDef]" = globs.get(pname)
            if pdef is None:
                thrower(False, pname)
            m = pdef.symtable.get(name)
            pname = pdef.parent
        return m

    def lookup_members(self, name, globs, thrower):
        # type: (str, GlobalClassTable,Callable[[bool,str],NoReturn]) -> 'Generator[ClassMember, None, None]'
        m = self.symtable.get(name)
        pdef: Optional[TypeDef] = self
        pname = self.parent
        while True:
            if m is not None:
                yield m
            if pname is None:
                thrower(True, name)
            pdef = globs.get(pname)
            if pdef is None:
                thrower(False, pname)
            m = pdef.symtable.get(name)
            pname = pdef.parent

    def mro(self, env: "GlobalClassTable") -> "Generator[str, None, List[str]]":
        yield self.name
        mro: "List[str]" = [self.name]
        parent = self.parent
        while parent:
            assert parent not in mro, f"Cyclic inherit? {parent}*2 in {self.name}.mro?"
            yield parent
            mro.append(parent)
            parent_cls: Optional[TypeDef] = env.get(parent)
            assert parent_cls is not None, f"no {parent} class in table?"
            parent = parent_cls.parent
        return mro


@dataclass
class FuncDef:
    __slots__ = (
        "name",
        "type",
        "typecheck",
        "is_class",
        "is_func",
        "is_var",
        "is_expr",
        "is_static",
        "contg_type",
    )

    def __init__(self, n: str, s: bool, sig: "FuncType", chk: "FuncTypeCheck", cls: str) -> None:
        self.name: Final[str] = n

        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[True]]" = True
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[False]]" = False

        self.contg_type = cls  # containing type
        self.type: Final["FuncType"] = sig
        self.typecheck: Final["FuncTypeCheck"] = chk
        self.is_static: Final[bool] = s


"""
None is for non-constant.
... is error
NotImplemented is not evaluated yet.
"""
COMPILE_CONSTANT = Union[bool, int, float, str, None, "ellipsis"]

_LocalVar = TypeVar("_LocalVar", "PyLit[True]", "PyLit[False]")
_StaticField = TypeVar("_StaticField", "PyLit[True]", "PyLit[False]")
_ContgCls = TypeVar("_ContgCls", "str", "None")
_FinalVar = TypeVar("_FinalVar", "PyLit[True]", "PyLit[False]")
_HasAstVal = TypeVar("_HasAstVal", "Expr", "None")


@dataclass
class VarDefGeneric(Generic[_LocalVar, _StaticField, _ContgCls, _FinalVar, _HasAstVal]):
    __slots__ = (
        "name",
        "type",
        "_typecheck",
        "is_class",
        "is_func",
        "is_var",
        "is_expr",
        "is_local",
        "contg_type",
        "is_static",
        "is_final",
        "ast_value",
        "_value",
        "erroneous",
    )

    @overload
    def __init__(self, name, type_, chker, final, ast):
        # type: (str,Type,BkoolTypeCheck[Type],_FinalVar,_HasAstVal) -> None
        ...

    @overload
    def __init__(self, name, type_, chker, final, ast, cls, stat):
        # type: (str,Type,BkoolTypeCheck[Type],_FinalVar,_HasAstVal,_ContgCls,_StaticField) -> None
        ...

    def __init__(self, name, type_, chker, final, ast, cls=None, stat=None):
        # type: (str,Type,BkoolTypeCheck[Type],_FinalVar,_HasAstVal,_ContgCls,Optional[_StaticField]) -> None
        self.name = name
        self.type = type_
        self._typecheck = chker
        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[True]]" = True
        self.is_expr: "Final[PyLit[False]]" = False

        self.is_local: _LocalVar = cls is None  # type: ignore
        self.contg_type: _ContgCls = cls  # type: ignore
        self.is_static: _StaticField = stat is True  # type: ignore

        self.is_final: _FinalVar = final
        self.ast_value: _HasAstVal = ast
        self._value: COMPILE_CONSTANT = NotImplemented if ast else None
        self.erroneous: bool = False

    def to_attr(self, stat: bool, cls: str) -> "Union[InstFieldType,StaticFieldType]":
        # Assume moved, don't use the old variable.
        self.is_local = False  # type: ignore
        self.is_static = stat  # type: ignore
        self.contg_type = cls  # type: ignore
        return self  # type: ignore

    def get_value(self, v: "ExprChecker", b: "Scoping") -> COMPILE_CONSTANT:
        if self.erroneous:
            return ...
        if self.is_final is True and self._value is NotImplemented:
            assert b.visited is not None
            assert self.ast_value is not None
            if self.contg_type is not None:
                this_attr = self.name, self.contg_type
                if any(equal(this_attr, a) for a in b.visited):
                    self.erroneous = True
                    self._value = ...
                    return ...
                local_b = b.Clone(v=(this_attr,))
            else:
                local_b = b
            expr = v.check(self.ast_value, local_b)
            assert expr.is_expr is True or expr.is_var is True
            self._value = expr.get_value(v, local_b)
            assert self._value is not None, "???"
            self.erroneous = self._value is ...
        return self._value

    @property
    def typecheck(self) -> "BkoolTypeCheck[Type]":
        return self._typecheck


LocalVarDefType = VarDefGeneric["PyLit[True]", "PyLit[False]", None, "PyLit[False]", "None"]
LocalConstDefType = VarDefGeneric["PyLit[True]", "PyLit[False]", None, "PyLit[True]", "Expr"]
LocalDefType = Union[LocalVarDefType, LocalConstDefType]

StaticVarDefType = VarDefGeneric["PyLit[False]", "PyLit[False]", "str", "PyLit[False]", "None"]
StaticConstDefType = VarDefGeneric["PyLit[False]", "PyLit[False]", "str", "PyLit[True]", "Expr"]
StaticFieldType = Union[StaticVarDefType, StaticConstDefType]

InstVarDefType = VarDefGeneric["PyLit[False]", "PyLit[True]", "str", "PyLit[False]", "None"]
InstConstDefType = VarDefGeneric["PyLit[False]", "PyLit[True]", "str", "PyLit[True]", "Expr"]
InstFieldType = Union[InstVarDefType, InstConstDefType]

VarDef = Union[LocalDefType, StaticFieldType, InstFieldType]


def LocalVar(name, type_, chker):
    # type: (str,Type,BkoolTypeCheck[Type]) -> LocalVarDefType
    return LocalVarDefType(name, type_, chker, False, None)


def LocalConst(name, type_, chker, ast):
    # type: (str,Type,BkoolTypeCheck[Type],Expr) -> LocalConstDefType
    return LocalConstDefType(name, type_, chker, True, ast)


@dataclass
class ExprNode:
    __slots__ = (
        "is_class",
        "is_func",
        "is_var",
        "is_expr",
        "type",
        "_typecheck",
        "is_final",
        "has_literal_value",
        "ast_value",
        "_value",
    )

    def __init__(self, ast, type_, final, lit, val, typchk):
        # type: (Expr, Type, bool, bool, COMPILE_CONSTANT, Optional[BkoolTypeCheck[Type]]) -> None

        self.ast_value = ast

        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[True]]" = True

        self.type: Final[Type] = type_
        self.is_final = final
        self.has_literal_value = lit
        self._typecheck = typchk
        assert (lit and val is not None) or (not lit)
        self._value: COMPILE_CONSTANT = val

    @property  # for evaluation when needed
    def typecheck(self) -> "BkoolTypeCheck[Type]":
        if self._typecheck is None:
            self._typecheck = _get_typecheck(self.type)
        return self._typecheck

    def get_value(self, _: "ExprChecker", __: "Scoping") -> COMPILE_CONSTANT:
        return self._value

    @property
    def name(self) -> "NoReturn":
        raise AssertionError("Oh no!")


ClassMember = Union[FuncDef, VarDef]
TrueSymbol = Union[TypeDef, FuncDef, VarDef]
SymtableEntry = TypeVar("SymtableEntry", TypeDef, ClassMember, TrueSymbol, covariant=True)
SymtableEntryInvariant = TypeVar("SymtableEntryInvariant", TypeDef, ClassMember, TrueSymbol)


class GenericSymtable(Generic[SymtableEntry], Dict[str, SymtableEntry]):  # type: ignore
    _R = TypeVar("_R", "SymbolTable", "ClassTable", "GlobalClassTable")

    @classmethod
    def FromList(cls, syms: "Sequence[SymtableEntry]") -> "GenericSymtable[SymtableEntry]":
        return cls([(s.name, s) for s in syms])

    def type_away(self, _: "TypeOf[GenericSymtable._R]") -> "GenericSymtable._R":
        return cast(GenericSymtable._R, self)

    def add_symbol(self, s: SymtableEntryInvariant) -> "GenericSymtable[SymtableEntryInvariant]":
        """Lose original type! At least, no type: ignore"""
        val = cast(GenericSymtable[SymtableEntryInvariant], self)
        return GenericSymtable[SymtableEntryInvariant]({**val, **{s.name: s}})

    def add(self, s: SymtableEntry) -> "GenericSymtable[SymtableEntry]":  # type: ignore
        return GenericSymtable[SymtableEntry]({**self, **{s.name: s}})

    def clone(self) -> "GenericSymtable[SymtableEntry]":
        return GenericSymtable[SymtableEntry]({**self})

    def merge(self, s: "GenericSymtable[SymtableEntry]") -> "GenericSymtable[SymtableEntry]":
        return GenericSymtable[SymtableEntry]({**self, **s})


# It's all hack, beneath it's all GenericSymtable
# Pycharm loses type hint
# Visual studio and vscode's pylance is much smarter
GlobalClassTable = GenericSymtable[TypeDef]  # Read: (Global classes) table
# Read: Class' members table # type: ignore
ClassTable = GenericSymtable[ClassMember]
SymbolTable = GenericSymtable[TrueSymbol]


class Scoping:
    __slots__ = (
        "is_static",
        "return_type",
        "parent",
        "enclosing",
        "visited",
        "globals",
        "symtab",
        "flow",
        "loop_depth",
        "is_left",
    )

    def __init__(
        self,
        *,
        stat: bool,
        ecls: Optional[str],
        rtype: Optional[Type],
        syms: SymbolTable,
        globs: GlobalClassTable,
        parent: Optional["Scoping"],
        visited: Optional[Tuple[Tuple[str, str], ...]] = None,
        loop_depth: int = 0,
        fl: Optional[ControlBlock] = None,
        lhs: bool = False,
    ) -> None:
        self.is_static: Final = stat
        self.return_type: Final[Optional[Type]] = rtype

        self.parent: Final[Optional["Scoping"]] = parent

        self.enclosing: Final[Optional[str]] = ecls

        self.visited: Optional[Tuple[Tuple[str, str], ...]] = visited
        """ class A:        |class B:         |class C:
        ->  const A = B.B   |  const B = C.C  |  const C = A.A
        ->  final int a0 = this.a1;
        ->  final int a1 = this.a0 + A.a;
        visit A = B.B -> visit B.B -> visit C.C -> visit A.A -> circular!
        use dfs visited to check.
        """

        self.globals: Final[GlobalClassTable] = globs

        self.symtab: Final[SymbolTable] = syms

        # control flow stuff
        self.flow: ControlBlock = fl if fl else NotImplemented  # type: ignore
        self.loop_depth = loop_depth
        self.is_left: bool = lhs

        ...

    def Clone(
        self,
        *,
        tab: Optional[SymbolTable] = None,
        pa: "Optional[Scoping]" = None,
        ecls: Optional[str] = None,
        stat: Optional[bool] = None,
        r: Optional[Type] = None,
        depth: Optional[int] = None,
        lhs: Optional[bool] = None,
        v: Optional[Tuple[Tuple[str, str], ...]] = None,
        fl: Optional[ControlBlock] = None,
        globs: Optional[GlobalClassTable] = None,
    ) -> "Scoping":
        s_ = self.is_static if stat is None else stat
        r_ = self.return_type if r is None else r
        ecls_ = self.enclosing if ecls is None else ecls
        d_ = self.loop_depth if depth is None else depth
        l_ = self.is_left if lhs is None else lhs
        """somehow mypy lose type of st_ below"""
        st_: SymbolTable = self.symtab if tab is None else tab  # type: ignore
        p_ = self.parent if pa is None else pa
        gls_ = self.globals if globs is None else globs
        v_ = self.visited if v is None else (v if self.visited is None else self.visited + v)
        fl_ = fl if fl else self.flow
        return Scoping(
            stat=s_,
            ecls=ecls_,
            rtype=r_,
            syms=st_,
            lhs=l_,
            parent=p_,
            globs=gls_,
            loop_depth=d_,
            visited=v_,
            fl=fl_,
        )

    def BranchDown(
        self,
        *,
        tab: Optional[SymbolTable] = None,
        ecls: Optional[str] = None,
        stat: Optional[bool] = None,
        r: Optional[Type] = None,
        depth: Optional[int] = None,
        lhs: Optional[bool] = None,
        v: Optional[Tuple[Tuple[str, str]]] = None,
        fl: Optional[ControlBlock] = None,
        globs: Optional[GlobalClassTable] = None,
    ) -> "Scoping":
        return self.Clone(
            tab=tab,
            fl=fl,
            ecls=ecls,
            stat=stat,
            r=r,
            pa=self,
            depth=depth,
            lhs=lhs,
            v=v,
            globs=globs,
        )

    def lookup(self, name: str) -> Optional[Symbol]:
        symbol = self.symtab.get(name)
        return symbol if symbol else (self.parent.lookup(name) if self.parent else None)

    def exist(self, name: str) -> bool:
        return (name in self.symtab) or (self.parent is not None and self.parent.exist(name))
