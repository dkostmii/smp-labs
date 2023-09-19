from calc import CalculatorState
from typing import Any


def clear_memory_proc(config: dict[str, Any], state: CalculatorState) -> None:
    if state.has_in_memory():
        state.clear_memory()


def save_to_memory_proc(config: dict[str, Any], state: CalculatorState):
    if len(state.history) < 1:
        print("Nothing to write to memory. No operation performed.")
        return

    entry = state.history[-1]

    if entry.result is None:
        print("Last operation has error. Please perform new operation to save to memory.")

    state.save_to_memory(entry.result)
