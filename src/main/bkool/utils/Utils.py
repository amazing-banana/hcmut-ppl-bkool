from typing import Any, List, Callable, Optional


class Utils:
    def lookup(
        self, name: str, lst: List[Any], func: Callable[[str], Any]
    ) -> Optional[Any]:
        for x in lst:
            if name == func(x):
                return x
        return None
