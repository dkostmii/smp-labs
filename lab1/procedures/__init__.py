from typing import Any, Callable

from lab1.domain.state import CalculatorState

from . import calc, config, exit_proc, history_proc, memory

Procedure = Callable[[dict[str, Any], CalculatorState], None]

__all__ = [
    "calc",
    "config",
    "exit_proc",
    "history_proc",
    "memory",
]
