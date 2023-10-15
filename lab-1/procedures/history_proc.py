from typing import Any

from domain.state import CalculatorState


def display_history_proc(config: dict[str, Any], state: CalculatorState) -> None:
    history_count = int(config["history_count"])
    print(f"Last {history_count} entries are:")

    for entry in state.history:
        entry_str = entry.fmt(config)
        print(entry_str)
