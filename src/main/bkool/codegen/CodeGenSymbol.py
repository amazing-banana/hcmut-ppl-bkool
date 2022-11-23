from dataclasses import dataclass  # beware! does not work for py < 3.7
from typing import (
    TYPE_CHECKING,
    Optional as Opt,
    Tuple,
    Union,
    TypeVar,
    Generic,
    Dict,
    Sequence,
)

from AST import *
from AdditionalTypes import *
from Frame import Frame
from ReachableFlow import ReachableFlow
from ShortCircuitLabel import SCLabel
from Visitor import Visitor

COMPILE_CONSTANT = Union[bool, int, float, str]

if TYPE_CHECKING:
    from typing import Literal as PyLit
    from typing import (
        Dict,
        Generator,
        List,
        Final,
        Sequence,
        Type as TypeOf,
        TypeVar,
        TYPE_CHECKING,
        cast,
        Tuple,
        Generic,
        Union,
    )
    from Emitter import Emitter  # type: ignore


def equal(_a: Tuple[str, str], _b: Tuple[str, str]) -> bool:
    # Same class, same name
    return _a[0] == _b[0] and _a[1] == _b[1]


class Context:
    frame: "Frame"
    is_static: "bool"
    enclosing: "Opt[str]"
    return_type: "Opt[Type]"
    symtable: "EnvTable"
    globs: "GlobalClassTable"


class Access(Context):
    def __init__(
            self,
            *,
            f: "Frame",
            s: "bool",
            e: "Opt[str]",
            r: "Opt[Type]",
            st: "EnvTable",
            gl: "GlobalClassTable",
            sto: "bool",
            fs: "Opt[Tuple[Tuple[str, str], ...]]" = None,
            emit: "Emitter" = NotImplemented,
            sc: "Opt[SCLabel]" = None,
            fl: "Opt[ReachableFlow]" = None,
    ) -> None:
        self.frame = f
        self.is_static = s
        self.enclosing = e
        self.return_type = r
        self.symtable = st
        self.globs = gl
        self.emit = emit
        self.visited: "Tuple[Tuple[str, str], ...]" = fs if fs else ()
        self.is_store: bool = sto
        self.sc: "SCLabel" = sc if sc else SCLabel()
        self.flow: "ReachableFlow" = fl if fl else ReachableFlow()
        ...

    def Clone(
            self,
            *,
            f: "Opt[Frame]" = None,
            s: "Opt[bool]" = None,
            e: "Opt[str]" = None,
            r: "Opt[Type]" = None,
            st: "Opt[EnvTable]" = None,
            gl: "Opt[GlobalClassTable]" = None,
            emit: "Opt[Emitter]" = None,
            sto: Opt[bool] = None,
            v: "Opt[Tuple[str,str]]" = None,
            sc: "Opt[SCLabel]" = None,
            fl: "Opt[ReachableFlow]" = None,
    ) -> "Access":
        s_ = self.is_static if s is None else s
        e_ = e if e is not None else self.enclosing
        f_ = f if f else self.frame
        r_ = r if r else self.return_type
        st_: "EnvTable" = st if st else self.symtable  # type: ignore
        gl_ = gl if gl else self.globs
        emit_ = emit if emit else self.emit
        sto_ = self.is_store if sto is None else sto
        v_ = self.visited if v is None else (v,) + self.visited
        sc_ = self.sc if sc is None else sc
        fl_ = self.flow if fl is None else fl
        return Access(
            f=f_, s=s_, e=e_, r=r_, st=st_, gl=gl_, sto=sto_, fs=v_, emit=emit_, fl=fl_, sc=sc_
        )


Node = Union["TypeDef", "FuncDef", "VarDef", "Exprs"]


class Exprs:
    def __init__(
            self,
            ast: Expr,
            t: Type,
            is_primitive_literal: "Opt[bool]" = None,
            codes: "Opt[Tuple[str, ...]]" = None,
    ):
        self.ast = ast

        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[True]]" = True
        self.type = t
        self.has_literal_value = is_primitive_literal
        self.codes: Tuple[str, ...] = codes if codes else ()

    def get_ast_value(self, _: Visitor, __: Access) -> "Opt[Expr]":
        return self.ast

    pass


class Symbol:
    name: str
    pass


@dataclass
class TypeDef(Symbol):
    def __init__(self, name: str, parent: Opt[str], syms: "ClassTable") -> None:
        self.name: Final[str] = name
        self.ast = Id(name)
        self.is_class: "Final[PyLit[True]]" = True
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[False]]" = False
        self.parent: Final[Opt[str]] = parent
        self.codes: "Final[Tuple[str, ...]]" = ()
        self.symtable: Final[ClassTable] = syms

    def lookup_member(self, name, globs):
        # type: (str, GlobalClassTable) -> 'ClassMember'
        m = self.symtable.get(name)
        pname = self.parent
        while m is None:
            assert pname is not None
            pdef = globs.get(pname)
            assert pdef is not None
            m = pdef.symtable.get(name)
            pname = pdef.parent
        return m

    def mro(self, env: "GlobalClassTable") -> "Generator[str, None, None]":
        yield self.name
        parent = self.parent
        while parent:
            yield parent
            parent_cls = env.get(parent)
            assert parent_cls is not None, f"no {parent} class in table?"
            parent = parent_cls.parent
    pass


@dataclass
class FuncDef(Symbol):
    def __init__(self, n: str, s: bool, sig: "FuncType", cls: str) -> None:
        self.name: Final[str] = n
        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[True]]" = True
        self.is_var: "Final[PyLit[False]]" = False
        self.is_expr: "Final[PyLit[False]]" = False
        self.contg_type = cls  # containing type
        self.type: Final["FuncType"] = sig
        self.is_static: Final[bool] = s

    pass


_LocalVar = TypeVar("_LocalVar", "int", "None")
_StaticField = TypeVar("_StaticField", "PyLit[True]", "PyLit[False]")
_ContgCls = TypeVar("_ContgCls", "str", "None")
_FinalVar = TypeVar("_FinalVar", "PyLit[True]", "PyLit[False]")
_HasAstVal = TypeVar("_HasAstVal", "Expr", "None")


@dataclass
class VarDefGeneric(Generic[_LocalVar, _StaticField, _ContgCls, _FinalVar, _HasAstVal], Symbol):
    def __init__(self, name, type_, index, stat, cls, final_, ast_val):
        # type: (str, Type, _LocalVar, _StaticField, _ContgCls, _FinalVar, _HasAstVal) -> None
        self.name = name
        self.ast = Id(name)
        self.type: Final[Type] = type_

        self.is_class: "Final[PyLit[False]]" = False
        self.is_func: "Final[PyLit[False]]" = False
        self.is_var: "Final[PyLit[True]]" = True
        self.is_expr: "Final[PyLit[False]]" = False

        self.ast_val: _HasAstVal = ast_val
        self.is_static: _StaticField = stat

        self.contg_type: _ContgCls = cls
        self.local_index: _LocalVar = index

        self.is_final: _FinalVar = final_
        self.has_literal_value: Opt[bool] = None if final_ else final_

    def to_attr(self, stat: bool, contg_cls: str) -> "Union[InstFieldType,StaticFieldType]":
        # Assume moved, don't use the old variable.
        self.local_index = None  # type: ignore
        self.is_static = stat  # type: ignore
        self.contg_type = contg_cls  # type: ignore
        return self  # type: ignore

    def get_ast_value(self, v: Visitor, ac: Access) -> "Opt[Expr]":
        if self.has_literal_value is True:  # { True | False | None }
            return self.ast_val
        elif self.has_literal_value is False:
            return None
        if self.contg_type is not None:
            f = (self.name, self.contg_type)
            if any(equal(e, f) for e in ac.visited):
                self.has_literal_value = False
                return None
            access = ac.Clone(v=f)
        else:
            access = ac

        expr_node: "Exprs" = v.visit(self.ast_val, access)
        if expr_node.has_literal_value:
            if isinstance(self.type, FloatType) and isinstance(expr_node.ast, IntLiteral):
                self.ast_val = FloatLiteral(float(expr_node.ast.value))  # type: ignore
            else:
                self.ast_val = expr_node.ast  # type: ignore
        else:
            self.ast_val = None  # type: ignore

        self.has_literal_value = isinstance(
            self.ast_val, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)
        )
        return self.ast_val


LocalVarDefType = VarDefGeneric["int", "PyLit[False]", None, "PyLit[False]", "None"]
LocalConstDefType = VarDefGeneric["int", "PyLit[False]", None, "PyLit[True]", "Expr"]
LocalDefType = Union[LocalVarDefType, LocalConstDefType]

StaticVarDefType = VarDefGeneric["None", "PyLit[False]", "str", "PyLit[False]", "None"]
StaticConstDefType = VarDefGeneric["None", "PyLit[False]", "str", "PyLit[True]", "Expr"]
StaticFieldType = Union[StaticVarDefType, StaticConstDefType]

InstVarDefType = VarDefGeneric["None", "PyLit[True]", "str", "PyLit[False]", "None"]
InstConstDefType = VarDefGeneric["None", "PyLit[True]", "str", "PyLit[True]", "Expr"]
InstFieldType = Union[InstVarDefType, InstConstDefType]

VarDef = Union[LocalDefType, StaticFieldType, InstFieldType]


def LocalVar(name, type_, index):
    # type: (str, Type, int) -> LocalVarDefType
    return LocalVarDefType(name, type_, index, False, None, False, None)


def LocalConst(name, type_, index, ast):
    # type: (str, Type, int, Expr) -> LocalConstDefType
    return LocalConstDefType(name, type_, index, False, None, True, ast)


ClassMember = Union[FuncDef, VarDefGeneric]
Env = Union[VarDefGeneric, TypeDef]
TrueSymbol = Union[TypeDef, FuncDef, VarDefGeneric]
SymtableEntry = TypeVar("SymtableEntry", TypeDef, ClassMember, Env, TrueSymbol, covariant=True)
SymtableEntryInvariant = TypeVar("SymtableEntryInvariant", TypeDef, ClassMember, Env, TrueSymbol)


class GenericSymtable(Generic[SymtableEntry], Dict[str, SymtableEntry]):  # type: ignore
    _R = TypeVar("_R", "SymbolTable", "ClassTable", "GlobalClassTable")

    @classmethod
    def FromList(Cls, syms: Sequence[SymtableEntry]) -> "GenericSymtable[SymtableEntry]":
        return Cls([(s.name, s) for s in syms])

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


GlobalClassTable = GenericSymtable[TypeDef]  # Read: (Global classes) table
ClassTable = GenericSymtable[ClassMember]  # type: ignore # Read: Class' members table
EnvTable = GenericSymtable[Union[VarDefGeneric, TypeDef]]
SymbolTable = GenericSymtable[TrueSymbol]
