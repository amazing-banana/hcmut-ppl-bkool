from dataclasses import dataclass  # beware! does not work for py < 3.7
from typing import Any, Dict, Final, Sequence

from AST import *

__all__ = ["FuncType", "ArraysOfDefault", "NullType", "AnyType", "AnyRefType", "FlexibleType"]


@dataclass
class FuncType(Type):
    __slots__ = ("param_types", "return_type")

    def __init__(self, p: Sequence[Type], r: Type):
        self.param_types = p
        self.return_type = r

    def __str__(self):
        to_str = "F[("
        to_str += ", ".join(repr(e) for e in self.param_types)
        to_str += ")=>" + repr(self.return_type) + "]"
        return to_str

    def __repr__(self):
        return str(self)

    pass


@dataclass
class FlexibleType(Type):
    __slots__ = ("inner", "dynamic")

    def __init__(self, wrap: "Type" = NotImplemented, dyn: "bool" = False):
        self.inner: "Type" = wrap
        self.dynamic = dyn

    def __str__(self):
        return f"Flexible({self.inner})"

    def __repr__(self):
        return f"Flexible({self.inner})"

    pass


class ArraysOfDefault(Expr):
    """For codegen, initialising array of ref type, because
    array of ref can't be initialised with literal syntax.
    """
    __slots__ = "array_type"

    def __init__(self, array_type: ArrayType) -> None:
        self.array_type = array_type

    def __str__(self):
        return f"ArraysOfDefault({self.array_type})"

    def __repr__(self):
        return f"ArraysOfDefault({self.array_type})"


class NullType(Type):
    def __str__(self):
        return "NullType()"

    def __repr__(self):
        return "NullType()"

    pass


class AnyRefType(Type):
    def __str__(self):
        return "AnyRefType()"

    def __repr__(self):
        return "AnyRefType()"

    pass


class AnyType(Type):
    def __str__(self):
        return "AnyType()"

    def __repr__(self):
        return "AnyType()"

    pass


class Singleton(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Null(metaclass=Singleton):
    """For distinguishing null from not having value at all"""

    ...


class Self(metaclass=Singleton):
    ...


NS: "Final[Null]" = Null()  # Null Singleton
SS: "Final[Self]" = Self()  # Self Singleton
