from os.path import exists
from typing import Any

from domain.history import HistoryEntry, read_history, write_history


class CalculatorState:
    def __init__(self):
        self.hist_file = ".calchist"
        self.memory: list[float] = []
        self.history: list[HistoryEntry] = []

        if exists(self.hist_file):
            self.history = read_history(self.hist_file)

    def has_in_memory(self) -> bool:
        return len(self.memory) > 0

    def get_memory(self) -> float:
        if not self.has_in_memory():
            raise Exception("Expected non-empty memory")
        return self.memory.pop()

    def clear_memory(self) -> None:
        self.memory.clear()

    def save_to_memory(self, value: float) -> None:
        self.memory.append(value)

    def add_history_entry(
        self, entry: HistoryEntry, config_opts: dict[str, Any]
    ) -> None:
        while len(self.history) >= config_opts["history_count"]:
            self.history.pop(0)

        self.history.append(entry)
        write_history(self.history, ".calchist")
