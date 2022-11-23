from contextlib import contextmanager
from functools import reduce
from typing import TYPE_CHECKING, List

from Frame import Frame

if TYPE_CHECKING:
    from typing import Optional, Generator
    from typing_extensions import TypeAlias

    NotImplementedType: "TypeAlias" = type(NotImplemented)  # type: ignore


class BoolContext:
    __slots__ = ("depth", "ops", "current_last_operand", "true_labels", "false_labels")

    def __init__(self, d: int = -1):
        # (depth: 0 (depth:1 a && b) || (depth:1 c && d)
        self.depth = d

        # when visit b: value = [False, True]
        # when visit (c && d): value = [True]
        # when visit c: value = [True, False]
        # when visit d: value = [True, True]
        # modified by push_labels() and enter_bool_expr()
        self.current_last_operand: List[bool] = []

        # Ops:
        #   when visit b: value = [||, &&]
        #   when visit (c && d): value = [&&]
        self.ops: "List[Optional[str]]" = []
        self.true_labels: "List[int]" = []
        self.false_labels: "List[int]" = []

    def __str__(self):
        return f"Bc({str((self.depth, self.ops, self.current_last_operand))})"

    def __repr__(self):
        return str(self)


class SCLabel:
    # Short Circuit true_label manager
    def __init__(self) -> None:
        self.context: "List[BoolContext]" = [BoolContext()]

    def is_current_root(self):
        return not self.context[-1].depth  # depth == 0

    def absolute_last(self):
        if self.context[-1].current_last_operand:
            # All true
            return reduce(lambda a, e: a and e, self.context[-1].current_last_operand)
        else:
            # var a = (b > c); standalone expr
            return True

    def is_current_last(self) -> "bool":
        # self.context[-1].current_last_operand == [] <=> var a = (b > c);
        return (not self.context[-1].current_last_operand) or (
            self.context[-1].current_last_operand[-1]
        )

    def upper_op_or_none(self) -> "Optional[str]":
        """[(_ && _) || (_ && _)] && [(_ && _) || (_ &&_ )]
        '         ^->^
        """
        if len(self.context[-1].ops) > 1:
            return self.context[-1].ops[-2]
        else:
            """var a = b > 0"""
            return None

    def op_for_last_expr_or_none(self) -> "Optional[str]":
        is_last_list = self.context[-1].current_last_operand
        index = len(is_last_list) - 1
        while index > -1:
            if not is_last_list[index]:
                break
            else:
                index -= 1
        if index > -1:
            """
            [(a &2& b) |1| (c &2& d)] &0& [(e &2& f) |1| (g &2& h)]
            '       ^[(False, &0&), (False, |1|), (True, &2&)]
            '       b => ||, if b true, jump to next [...]
            
            '                     d^[False, True, True] if d is false => jump to false immediately
            '                               e^[True, False, False]
            """
            return self.context[-1].ops[index]
        elif next(iter(self.context[-1].current_last_operand), False):
            """
            [(a && b) || (c && d)] && [(e && f) || (g && h)]
            '                          [True, True, True]^
            [] => next(iter([],False) == False
            """
            return self.context[-1].ops[0]
        else:
            """var a = (b > c)"""
            return None

    def get_current_labels(self) -> "tuple[int, int]":
        return (
            self.context[-1].true_labels[-1],
            self.context[-1].false_labels[-1],
        )

    @contextmanager
    def push_label_context(self, true_label: int, false_label: int, last=False):
        self.context[-1].true_labels.append(true_label)
        self.context[-1].false_labels.append(false_label)
        self.context[-1].current_last_operand.append(last)
        yield
        self.context[-1].true_labels.pop()
        self.context[-1].false_labels.pop()
        self.context[-1].current_last_operand.pop()

    @contextmanager
    def enter_bool_expr(self, f, labels=None, op=None, last=None):
        # type: (Frame,Optional[tuple[int,int]],Optional[str],Optional[bool]) -> Generator[tuple[int,int], None, None]
        """expr = (a && b && c) || (d && e) || (f && g)
        def visitBinary(expr):
            if op in {||, &&}:
            with enter_bool_expr(...):
                 exprs = flatten expr op
                 ...
                 for each e in exprs do visit(e)
        """
        self.context[-1].depth += 1

        if self.context[-1].depth == 0:
            true_label = labels[0] if labels is not None else f.getNewLabel()
            false_label = labels[1] if labels is not None else f.getNewLabel()
            self.context[-1].true_labels.append(true_label)
            self.context[-1].false_labels.append(false_label)

        self.context[-1].ops.append(op)
        if last is not None:
            self.context[-1].current_last_operand.append(last)

        yield self.context[-1].true_labels[-1], self.context[-1].false_labels[-1]

        self.context[-1].depth -= 1

        self.context[-1].ops.pop()
        if last is not None:
            self.context[-1].current_last_operand.pop()

        if self.context[-1].depth < 0:
            self.context[-1].true_labels.pop()
            self.context[-1].false_labels.pop()

    @contextmanager
    def enter_expr(self):
        if self.context[-1].depth != -1:
            self.context.append(BoolContext())
            yield
            self.context.pop()
        else:
            yield

    pass
