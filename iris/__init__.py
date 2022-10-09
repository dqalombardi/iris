"""Package containing utilities for printing to stdout in color."""

from enum import Enum
from typing import Any

__all__ = [
    "ANSIColor",
    "colored",
    "cprint",
]


class ANSIColor(Enum):
    """Enumeration of ANSI color codes."""

    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    PURPLE = "\033[95m"
    RED = "\033[91m"
    YELLOW = "\033[93m"


_ANSI_END = "\033[0m"


def colored(text: str, color: ANSIColor) -> str:
    """
    Returns a copy of the passed text colored with the passed color.
    Raises TypeError if passed color is not a member of `ANSIColor`.
    Note: Returned str will be 9 chars longer than passed `text` as coloring text in the terminal is additive in nature.
    """

    if not isinstance(color, ANSIColor):
        raise TypeError(f"Passed color '{color}' is not a member of {ANSIColor}")

    colored_text = f"{color.value}{text}{_ANSI_END}"

    return colored_text


_SEP_KW = "sep"
_END_KW = "end"


def cprint(
    *objects: object,
    color: ANSIColor,
    color_sep: bool = True,
    color_end: bool = True,
    **print_kwargs: Any,
) -> None:
    """
    Prints the passed `objects` to stdout in the passed `color`.
    Passing `color_sep` indicates that a passed custom kwarg `sep` should be colored.
    Passing `color_end` indicates that a passed custom kwarg `end` should be colored.
    All other passed `print_kwargs` will be passed directly to buitin print function.
    """

    # Coloring objects
    colored_objects = (colored(str(obj), color=color) for obj in objects)

    # Coloring sep if custom str
    passed_sep = print_kwargs.get(_SEP_KW, None)
    if color_sep and isinstance(passed_sep, str):
        colored_sep = colored(passed_sep, color=color)
        print_kwargs[_SEP_KW] = colored_sep

    # Coloring end if custom str
    passed_end = print_kwargs.get(_END_KW, None)
    if color_end and isinstance(passed_end, str):
        colored_end = colored(passed_end, color=color)
        print_kwargs[_END_KW] = colored_end

    # Sending colored args and kwargs to builtin print
    print(*colored_objects, **print_kwargs)

    return
