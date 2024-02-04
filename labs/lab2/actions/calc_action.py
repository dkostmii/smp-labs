from typing import Any

from domain.operation import apply_op
from labs.lab2.domain.history import HistoryEntry
from labs.lab2.domain.io import display_op_res, read_op
from labs.lab2.domain.state import CalculatorState
from std.result import Result


def calc_action(opts: dict[str, Any], state: CalculatorState) -> None:
    op, values = read_op(state)
    op_res = apply_op(op, values)

    match op_res:
        case float():
            entry_res = op_res
        case Result(is_ok=True):
            entry_res = op_res.ok
        case Result(is_err=True):
            entry_res = op_res.err
        case _:
            raise Exception("Invalid op_res")

    if entry_res is None:
        raise Exception(
            "Unreachable exception. Expected either float or OperationError"
        )

    entry = HistoryEntry(op, values, entry_res)
    state.add_history_entry(entry, opts)

    display_op_res(op_res, opts)
