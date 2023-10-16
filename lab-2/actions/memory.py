from typing import Any

from domain.state import CalculatorState
from std.result import Err


def clear_memory_action(_: dict[str, Any], state: CalculatorState) -> None:
    if state.has_in_memory():
        state.clear_memory()
        print("Memory cleared.")
    else:
        print("Nothing to clear.")


def save_to_memory_action(_: dict[str, Any], state: CalculatorState):
    if len(state.history) < 1:
        print("Nothing to write to memory. No operation performed.")
        return

    entry = state.history[-1]

    if entry.result is str or entry.result is Err:
        print(
            "Last operation has error. Please perform new operation to save to memory."
        )
        return

    try:
        value: float = float(entry.result)
        state.save_to_memory(value)
        print(f"Value {value} saved to memory.")
    except ValueError:
        print(
            "Last operation has error. Please perform new operation to save to memory."
        )
