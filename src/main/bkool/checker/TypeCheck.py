from abc import ABC
from functools import lru_cache
from typing import Final, Generic, TypeVar, TYPE_CHECKING, Optional, List

from AST import *
from AdditionalTypes import *

if TYPE_CHECKING:
    # avoid circular import at runtime for type hints
    from Symbolic import GlobalClassTable

    ...

__all__ = [
    "BkoolTypeCheck",
    "TBkool",
    "IntTypeCheck",
    "FloatTypeCheck",
    "BoolTypeCheck",
    "StringTypeCheck",
    "VoidTypeCheck",
    "AnyTypeCheck",
    "AnyRefTypeCheck",
    "NullTypeCheck",
    "ArrayTypeCheck",
    "ClassTypeCheck",
    "FuncTypeCheck",
    "FlexibleTypeCheck",
    "Int",
    "Float",
    "Bool",
    "String",
    "Void",
    "AnyRef",
    "Any",
    "Null",
]

TBkool = TypeVar(
    "TBkool",
    Type,
    IntType,
    FloatType,
    BoolType,
    StringType,
    VoidType,
    ArrayType,
    ClassType,
    FuncType,
    AnyType,
    AnyRefType,
    NullType,
    FlexibleType,
    covariant=True,
)

REF_TYPES = (NullType, ClassType, StringType, ArrayType, AnyRefType)


@lru_cache(maxsize=2)
def get_typevisitor():
    # avoid circular import
    from TypeCheker import TypeCheker as v

    return v()


class BkoolTypeCheck(ABC, Generic[TBkool]):
    def __init__(self, t: "TBkool"):
        self.type: "Final[TBkool]" = t

    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return self.type if isinstance(other, self.type.__class__) else None

    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return other if isinstance(self.type, (other.__class__, AnyType)) else None

    def is_same_type(self, t: Type) -> bool:
        other = t.inner if isinstance(t, FlexibleType) else t
        return isinstance(other, self.type.__class__)


class FlexibleTypeCheck(BkoolTypeCheck[FlexibleType]):
    def __init__(self, inst: "FlexibleType"):
        super().__init__(inst)
        self._visitor = get_typevisitor()
        self._inner_chk: "Optional[BkoolTypeCheck]" = None

    def override_type(self, do_override: "bool", t: "Optional[Type]"):
        if do_override:
            assert t
            self.type.inner = t
            self._inner_chk = self._visitor.check(t)
        pass

    def common_ancestor(self, t: Type, b: "GlobalClassTable"):
        base: "Type" = self.type.inner
        if isinstance(base, REF_TYPES) and isinstance(t, REF_TYPES):
            if isinstance(base, ClassType) and isinstance(t, ClassType):
                this = b[base.classname.name].mro(b)
                other = set(b[t.classname.name].mro(b))
                for c in this:
                    if c in other:
                        return ClassType(Id(c))
            return AnyRefType()
        return None

    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        self.override_type(self._inner_chk is None, t)
        assert self._inner_chk
        if self.type.dynamic:
            result = self._inner_chk.assign_from(t, b)
            if result is None:
                result = self.common_ancestor(t, b)
                self.override_type(result is not None, result)
            return result
        else:
            return self._inner_chk.assign_from(t, b)

    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        self.override_type(self._inner_chk is None, t)
        assert self._inner_chk
        return self._inner_chk.assign_to(t, b)


class IntTypeCheck(BkoolTypeCheck[IntType]):
    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return other if isinstance(other, (IntType, FloatType, AnyType)) else None


class BoolTypeCheck(BkoolTypeCheck[BoolType]):
    ...


class VoidTypeCheck(BkoolTypeCheck[VoidType]):
    ...


class AnyTypeCheck(BkoolTypeCheck[AnyType]):
    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        return t.inner if isinstance(t, FlexibleType) else t


class StringTypeCheck(BkoolTypeCheck[StringType]):
    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return other if isinstance(other, (StringType, AnyRefType, AnyType)) else None


class AnyRefTypeCheck(BkoolTypeCheck[AnyRefType]):
    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return self.type if isinstance(other, REF_TYPES) else None


class NullTypeCheck(BkoolTypeCheck[NullType]):
    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return other if isinstance(other, REF_TYPES) else None


class FloatTypeCheck(BkoolTypeCheck[FloatType]):
    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        other = t.inner if isinstance(t, FlexibleType) else t
        return self.type if isinstance(other, (IntType, FloatType)) else None


class ArrayTypeCheck(BkoolTypeCheck[ArrayType]):
    def __init__(self, t: ArrayType):
        super().__init__(t)
        self._ele_chker: Optional[BkoolTypeCheck[Type]]
        self._ele_chker = None

    @property
    def ele_chker(self) -> "BkoolTypeCheck[Type]":
        if self._ele_chker is None:
            self._ele_chker = get_typevisitor().check(self.type.eleType)
        return self._ele_chker

    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        t = t.inner if isinstance(t, FlexibleType) else t
        if isinstance(t, NullType):
            return self.type
        elif (not isinstance(t, ArrayType)) or self.type.size != t.size:
            return None

        ele_type = self.ele_chker.assign_from(t.eleType, b)
        return self.type if ele_type else None

    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        t = t.inner if isinstance(t, FlexibleType) else t
        if isinstance(t, (AnyRefType, AnyType)):
            return self.type
        elif (not isinstance(t, ArrayType)) or self.type.size != t.size:
            return None

        ele_type = self.ele_chker.assign_to(t.eleType, b)
        return self.type if ele_type else None

    def is_same_type(self, t: Type) -> bool:
        t = t.inner if isinstance(t, FlexibleType) else t
        return (
                isinstance(t, ArrayType)
                and self.type.size == t.size
                and self.ele_chker.is_same_type(t.eleType)
        )


class ClassTypeCheck(BkoolTypeCheck[ClassType]):
    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        t = t.inner if isinstance(t, FlexibleType) else t
        if isinstance(t, NullType):
            return self.type
        elif not isinstance(t, ClassType):
            return None

        name = self.type.classname.name
        if name == t.classname.name:
            return self.type
        rhs = b.get(t.classname.name)
        assert rhs is not None and rhs.is_class
        r_mro = rhs.mro(b)

        return self.type if name in r_mro else None

    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        t = t.inner if isinstance(t, FlexibleType) else t
        if isinstance(t, (AnyRefType, AnyType)):
            return self.type
        elif not isinstance(t, ClassType):
            return None

        name = self.type.classname.name
        if name == t.classname.name:
            return self.type
        lhs = b.get(self.type.classname.name)
        assert lhs is not None and lhs.is_class
        l_mro = lhs.mro(b)

        return t if t.classname.name in l_mro else None

    def is_same_type(self, t: Type) -> bool:
        return isinstance(t, ClassType) and t.classname.name == self.type.classname.name


class FuncTypeCheck(BkoolTypeCheck[FuncType]):
    """If S is a subtype of T, (SubType <: Type)
    S can safely be used in any op where a term of type T is expected.
    In other words: S is assignable to T
        F1:  (A1) -> R1
        F2:  (A2) -> R2
    => F2 <: F1 if A1 <: A2 and R2 <: R1
    ~~~ F2 is subtype___ of F1         | ~~  F2 is assignable to F1
        if A1 is subtype___ of A2      |     if A1 is assignable to A2
        and R2 is subtype___ of R1     |     and R2 is assignable to R1
    ex. (A2     -> R2 ) <: (A1  -> R1    )
    ex. (Animal -> Cat) <: (Cat -> Animal)
    (Animal -> Cat   ) is assignable to (Cat -> Animal)
    (Cat    -> Cat   ) is assignable to (Cat -> Animal)
    (Animal -> Animal) is assignable to (Cat -> Animal)
    """

    def __init__(self, t: FuncType):
        super().__init__(t)
        v = get_typevisitor()
        self.params: List[BkoolTypeCheck[Type]]
        self.params_chk = [v.check(p) for p in t.param_types]
        self.return_chk = v.check(t.return_type)

    def assign_from(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        # i.e. self.type is super-type of t,
        # example above: self.type is (Cat -> Animal)
        t = t.inner if isinstance(t, FlexibleType) else t
        if not isinstance(t, FuncType) or len(self.params_chk) != len(t.param_types):
            return None

        z = zip(self.params_chk, t.param_types)
        for param_chk, arg_t in z:
            if not param_chk.assign_to(arg_t, b):
                return None
        if self.return_chk.assign_from(t.return_type, b):
            return self.type
        else:
            return None

    def assign_to(self, t: Type, b: "GlobalClassTable") -> Optional[Type]:
        # i.e. self.type is subtype of t
        # example above: self.type is (Animal -> Animal)
        t = t.inner if isinstance(t, FlexibleType) else t
        if not isinstance(t, FuncType) or len(self.params_chk) != len(t.param_types):
            return None

        z = zip(self.params_chk, t.param_types)
        for param_chk, arg_t in z:
            if not param_chk.assign_from(arg_t, b):
                return None
        if self.return_chk.assign_to(t.return_type, b):
            return self.type
        else:
            return None

    def callable_with(self, args: List[Type], b: "GlobalClassTable") -> bool:
        # just subtyping of parameters
        return len(self.params_chk) == len(args) and all(
            param_chk.assign_from(arg_t, b) for param_chk, arg_t in zip(self.params_chk, args)
        )

    def not_callable_with(self, args: List[Type], b: "GlobalClassTable") -> bool:
        return len(self.params_chk) != len(args) or any(
            not formal.assign_from(args_t, b) for formal, args_t in zip(self.params_chk, args)
        )

    def is_same_type(self, t: Type) -> bool:
        return (
                isinstance(t, FuncType)
                and len(self.params_chk) == len(t.param_types)
                and all(
            formal.is_same_type(args_t)
            for formal, args_t in zip(self.params_chk, t.param_types)
        )
                and self.return_chk.is_same_type(t.return_type)
        )


Int = IntTypeCheck(IntType())
Float = FloatTypeCheck(FloatType())
Bool = BoolTypeCheck(BoolType())
String = StringTypeCheck(StringType())
Void = VoidTypeCheck(VoidType())
AnyRef = AnyRefTypeCheck(AnyRefType())
Any = AnyTypeCheck(AnyType())
Null = NullTypeCheck(NullType())
