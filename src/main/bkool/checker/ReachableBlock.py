from typing import TYPE_CHECKING, List, Optional, Tuple

if TYPE_CHECKING:
    pass


class ControlBlock:
    def __init__(self, context: str, c: "Optional[ControlBlock]" = None) -> None:
        self.stack: Tuple[ControlBlock, ...]
        self.block_exit: ControlBlock
        self.if_exit: ControlBlock
        self.break_exit: ControlBlock
        self.cont_exit: ControlBlock
        self.context: str

        if c is not NotImplemented:
            self.context = f"{c.context}.{context}" if c else context
            self.stack = ((self,) + c.stack) if c else (self,)
            self.paths_to_self: List[ControlBlock] = []
            self.unreachable = False
            self.block_exit = c if c else NotImplemented  # type: ignore
            self.if_exit = c.if_exit if c else NotImplemented  # type: ignore
            self.break_exit = c.break_exit if c else NotImplemented  # type: ignore
            self.cont_exit = c.cont_exit if c else NotImplemented  # type: ignore
        else:
            self.context = context
            self.stack = NotImplemented
            self.cont_exit = NotImplemented
            self.break_exit = NotImplemented
            self.if_exit = NotImplemented

    @property
    def reachable(self) -> bool:
        return not self.unreachable

    @reachable.setter
    def reachable(self, value: bool) -> None:
        self.unreachable = not value

    @property
    def is_unreachable(self) -> bool:
        return any(f.unreachable for f in self.stack)

    def mark_unreachable(self) -> None:
        self.unreachable = True

    def add_exit_path(self, dest: "ControlBlock"):
        c = ControlBlock(f"exit {self.context}", None)
        c.unreachable = any(p.unreachable for p in self.stack)
        dest.paths_to_self.append(c)
        ...

    def break_(self):
        self.add_exit_path(self.break_exit)
        self.unreachable = True

    def continue_(self):
        self.add_exit_path(self.cont_exit)
        self.unreachable = True

    def enter(self, if_: Optional[bool] = None, c: Optional[str] = None) -> "ControlBlock":
        return (
            IfBlock(self)
            if if_ is True
            else ForBlock(self)
            if if_ is False
            else ControlBlock(str(c), self)
        )

    def exit(self):
        if self.block_exit is not NotImplemented:
            self.add_exit_path(self.block_exit)


class IfBlock(ControlBlock):
    def __init__(self, c: "ControlBlock") -> None:
        super(IfBlock, self).__init__(f"{c.context}.if", NotImplemented)
        self.unreachable = False
        self.stack: Tuple[ControlBlock, ...] = (self,) + c.stack

        self.if_exit = c
        self.paths_to_self: List[ControlBlock] = []

        self.break_exit: ControlBlock = c.break_exit
        self.cont_exit: ControlBlock = c.cont_exit

    def exit(self):
        self.add_exit_path(self.if_exit)
        escapes = (
            [self.if_exit, *self.paths_to_self]
            if len(self.paths_to_self) == 1  # no elseStmt
            else self.paths_to_self
        )
        self.if_exit.reachable = any(e.reachable for e in escapes)


class ForBlock(ControlBlock):
    def __init__(self, c: "ControlBlock") -> None:
        super(ForBlock, self).__init__(f"{c.context}.for", NotImplemented)
        self.unreachable = False
        self.stack: Tuple[ControlBlock, ...] = (self,) + c.stack

        self.if_exit = c.if_exit
        self.paths_to_self: List[ControlBlock] = []
        self.break_exit: ControlBlock = c
        self.cont_exit: ControlBlock = self

    def exit(self):
        self.add_exit_path(self)
        escapes = [self.break_exit, *self.paths_to_self]
        self.break_exit.reachable = any(e.reachable for e in escapes)
