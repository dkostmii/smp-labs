from typing import Any
import json

from os.path import exists


class HistoryEntry:
    def __init__(self, operation_str: str, result: float | None):
        self.operation_str = operation_str
        self.result = result

    def toDict(self):
        return { "operation_str": self.operation_str, "result": self.result }


def entryFromDict(dictionary: dict[str, Any]):
    result = None

    match dictionary["result"]:
        case float():
            result = dictionary["result"]

    return HistoryEntry(
        operation_str=str(dictionary["operation_str"]),
        result=result)


def read_history(hist_file_path: str) -> list[HistoryEntry]:
    result: list[HistoryEntry] = []

    with open(hist_file_path, 'r') as f:
        data_dicts = json.load(f)

        for d in data_dicts:
            result.append(entryFromDict(d))

    return result


def write_history(history: list[HistoryEntry], hist_file_path: str) -> None:
    with open(hist_file_path, 'w') as f:
        json.dump([entry.toDict() for entry in history], f)


class CalculatorState:
    def __init__(self):
        self.hist_file = ".calchist"
        self.memory: list[float] = []
        self.history: list[HistoryEntry] = []

        if exists(self.hist_file):
            self.history = read_history(self.hist_file)


    def has_in_memory(self):
        return len(self.memory) > 0


    def get_memory(self) -> float:
        if not self.has_in_memory():
            raise Exception("Expected non-empty memory")
        return self.memory.pop()


    def clear_memory(self) -> None:
        self.memory.clear()


    def save_to_memory(self, value: float) -> None:
        self.memory.append(value)


    def add_history_entry(self, entry: HistoryEntry, config_opts: dict[str, Any]) -> None:
        while len(self.history) >= config_opts["history_count"]:
            self.history.pop(0)

        self.history.append(entry)
        write_history(self.history, ".calchist")

