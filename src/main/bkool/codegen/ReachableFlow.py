from contextlib import contextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Literal, Optional

    pass


class ReachableFlow:
    def __init__(self) -> None:
        # block[i] is unreachable
        self.blocks: "List[bool]" = [False]

        # Blocks that exit to block[i]
        self.to_block: List[List[bool]] = []

        self.breaks: List[int] = []

    @contextmanager
    def enter_block(
            self, *, kind: "Optional[Literal['func','if','for']]" = None
    ) -> "Generator[None,None,None]":
        pre_append_index = len(self.blocks) - 1

        if kind == "for":
            self.breaks.append(pre_append_index)

        self.blocks.append(False)
        self.to_block.append([])

        yield

        if kind == "func":
            return  # manually exit through self.method_exit()
        if kind != "for":
            self.add_exit_to(pre_append_index)

        self.blocks.pop()
        exit_to_this = self.to_block.pop()
        only_true_branch = len(exit_to_this) == 1

        assert kind != "if" or len(exit_to_this) in {1, 2}

        if (kind == "if" and only_true_branch) or kind == "for":
            exit_to_this.insert(0, self.blocks[-1])

        self.blocks[-1] = any(unreachable for unreachable in exit_to_this)

        if kind == "for":
            self.breaks.pop()
        
        return

    def method_exit(self):
        self.blocks.pop()
        self.to_block.pop()

    @property
    def is_unreachable(self) -> bool:
        return any(f for f in self.blocks)

    @property
    def is_reachable(self) -> bool:
        return not self.is_unreachable

    def mark_unreachable(self) -> None:
        self.blocks[-1] = True

    def add_exit_to(self, target: int):
        unreachable = any(unreachable for unreachable in self.blocks[target + 1:])
        self.to_block[target].append(unreachable)

    def handle_break(self):
        self.add_exit_to(self.breaks[-1])
        self.blocks[-1] = True

    def handle_continue(self):
        self.blocks[-1] = True
