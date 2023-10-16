from typing import Callable

from std.read import read_yes_no


def repeat_while_requested(
    action: Callable, title: str = "Do you want to continue?", default: bool = False
):
    repeat_requested = True

    while repeat_requested:
        action()
        repeat_requested = read_yes_no(title=title, default=default)
