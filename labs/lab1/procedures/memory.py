from typing import Any

from labs.lab1.domain.operation import OperationError
from labs.lab1.domain.state import CalculatorState


def clear_memory_proc(_: dict[str, Any], state: CalculatorState) -> None:
    if state.has_in_memory():
        state.clear_memory()
    else:
        print("Nothing to clear.")


def save_to_memory_proc(_: dict[str, Any], state: CalculatorState):
    if len(state.history) < 1:
        print("Nothing to write to memory. No operation performed.")
        return

    entry = state.history[-1]

    if entry.result is str:
        print(
            "Last operation has error. Please perform new operation to save to memory."
        )
        return

    try:
        value: float = float(entry.result)
        state.save_to_memory(value)
    except ValueError:
        print(
            "Last operation has error. Please perform new operation to save to memory."
        )
