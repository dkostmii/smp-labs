import json
from typing import Any

from lab1.domain.operation import fmt_operation
from lab1.domain.operator import Operator, get_operator, get_symbol
from std.result import Err


class HistoryEntry:
    def __init__(
        self, operator: Operator, values: tuple[float, ...], result: float | Err
    ):
        self.operator = operator
        self.values = values

        parsed_result: str | float = repr(Err(val=None))

        if isinstance(result, Err):
            parsed_result = repr(result)
        elif isinstance(result, float):
            parsed_result = float(result)
        else:
            raise Exception(f"Unexpected result type: {type(result)}")

        self.result = parsed_result

    def to_dict(self) -> dict[str, Any]:
        return {
            "operator": get_symbol(self.operator),
            "values": self.values,
            "result": self.result,
        }

    @staticmethod
    def from_dict(dictionary: dict[str, Any]):
        operator = get_operator(dictionary["operator"])

        if operator is None:
            raise Exception(f"Unknown operator: {dictionary['operator']}")

        values = dictionary["values"]
        result = dictionary["result"]

        if isinstance(result, str):
            result = Err(val=result.replace("Error: ", ""))

        return HistoryEntry(operator=operator, values=values, result=result)

    def fmt(self, opts: dict[str, Any]) -> str:
        return fmt_operation(self.values, self.operator, self.result, opts)


def read_history(hist_file_path: str) -> list[HistoryEntry]:
    result: list[HistoryEntry] = []

    with open(hist_file_path, "r") as f:
        data_dicts = json.load(f)

        for d in data_dicts:
            result.append(HistoryEntry.from_dict(d))

    return result


def write_history(history: list[HistoryEntry], hist_file_path: str) -> None:
    with open(hist_file_path, "w") as f:
        json.dump([entry.to_dict() for entry in history], f)
