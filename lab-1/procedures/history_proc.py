from typing import Any

from domain.history import HistoryEntry
from domain.state import CalculatorState


def display_history_proc(config: dict[str, Any], state: CalculatorState) -> None:
    history_count = int(config["history_count"])

    entries: list[HistoryEntry] = state.history

    if history_count == 0:
        print("History entries are:")
    else:
        print(f"Last {history_count} entries are:")
        entries = state.history[: history_count - 1]

    for entry in entries:
        entry_str = entry.fmt(config)
        print(entry_str)
