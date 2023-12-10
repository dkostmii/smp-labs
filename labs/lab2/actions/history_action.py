from typing import Any

from labs.lab2.domain.history import HistoryEntry
from labs.lab2.domain.state import CalculatorState


def history_action(config: dict[str, Any], state: CalculatorState) -> None:
    history_count = int(config["history_count"])

    entries: list[HistoryEntry] = state.history

    if history_count == 0:
        print("Displaying all history entries:")
    else:
        print(f"Displaying last {history_count} history entries:")
        entries = state.history[-history_count:]

    for entry in entries:
        entry_str = entry.fmt(config)
        print(entry_str)
