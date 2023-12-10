from typing import Any

from labs.lab1.domain.history import HistoryEntry
from labs.lab1.domain.state import CalculatorState


def display_history_proc(config: dict[str, Any], state: CalculatorState) -> None:
    history_count = int(config["history_count"])

    entries: list[HistoryEntry] = state.history

    if history_count == 0:
        print("History entries are:")
    else:
        print(f"Last {history_count} entries are:")
        entries = entries[-history_count:]

    for entry in entries:
        entry_str = entry.fmt(config)
        print(entry_str)
