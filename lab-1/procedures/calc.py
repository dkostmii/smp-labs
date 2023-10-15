from typing import Any

from domain.history import HistoryEntry
from domain.io import display_op_res, read_op
from domain.operation import apply_op
from domain.state import CalculatorState
from std.result import Err, Ok, Result


def do_calculation_proc(opts: dict[str, Any], state: CalculatorState) -> None:
    op, values = read_op(state)
    op_res = apply_op(op, values)

    entry_res: float | Err = Err(val=None)

    match op_res:
        case float():
            entry_res = op_res
        case Result(is_ok=True):
            if not isinstance(op_res.ok_val, Ok):
                raise Exception("Expected op_res.ok_val to be Ok")

            if not isinstance(op_res.ok_val.val, float):
                raise Exception("Expected op_res.ok_val.val to be float")

            entry_res = op_res.ok_val.val
        case Result(is_ok=False):
            if not isinstance(op_res.err_val, Err):
                raise Exception("Expected op_res.err_val to be Err")

            entry_res = op_res.err_val
        case _:
            raise Exception("Invalid op_res")

    entry = HistoryEntry(op, values, entry_res)
    state.add_history_entry(entry, opts)

    display_op_res(op_res, opts)
