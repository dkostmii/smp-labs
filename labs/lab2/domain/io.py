from typing import Any

from domain.decimals import get_formatter
from domain.operation import BinaryOperator, Operator, UnaryOperator, operators
from std.read import read_single_float, read_until_pred, read_yes_no
from std.result import Err, Ok, Result

from .state import CalculatorState


def read_num_or_memory(state: CalculatorState, title: str = "") -> float:
    if state.has_in_memory():
        confirmed = read_yes_no(
            f"The memory contains value [{state.memory[-1]}]. "
            + "Do you want to use that value?",
            default=False,
        )

        if confirmed:
            return state.get_memory()

    return read_single_float(title)


def read_nums(op: Operator, state: CalculatorState) -> tuple[float, ...]:
    match op:
        case BinaryOperator():
            left = read_num_or_memory(state, "Enter a first number: ")
            right = read_num_or_memory(state, "Enter a second number: ")
            return (left, right)

        case UnaryOperator():
            x = read_num_or_memory(state, "Enter a number: ")
            return (x,)

        case _:
            raise Exception("BinaryOperator or UnaryOperator expected")


def read_op(state: CalculatorState) -> tuple[Operator, tuple[float, ...]]:
    valid_ops = list(operators.keys())
    valid_ops_str = ", ".join(valid_ops)

    op_key = read_until_pred(
        lambda x: x in valid_ops,
        f"Choose an operation [{valid_ops_str}]: ",
        "Invalid operator. Try again",
    )
    op = operators[op_key]

    values = read_nums(op, state)

    return op, values


def display_err(err: Err) -> None:
    print(str(err))


def display_val(val: Ok | float, opts: dict[str, Any]) -> None:
    fmt = get_formatter(opts)
    match val:
        case Ok():
            return print(f"=> {fmt(val.val)}")
        case float():
            return print(f"=> {fmt(val)}")
        case _:
            raise ValueError("Ok or float expected")


def display_op_res(val: float | Result, opts: dict[str, Any]) -> None:
    match val:
        case Result():
            return val.map(lambda val: display_val(val, opts), display_err)
        case float():
            return display_val(val, opts)
        case _:
            raise Exception("Expected Result or float")
