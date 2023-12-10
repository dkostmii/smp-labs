from typing import Any

from std.result import Result

from .decimals import get_formatter
from .operator import BinaryOperator, Operator, UnaryOperator, get_symbol


def apply_op(op: Operator, values: tuple[float, ...]) -> float | Result:
    match op:
        case UnaryOperator():
            (x,) = values
            return op.apply(x)
        case BinaryOperator():
            (left, right) = values
            return op.apply(left, right)

        case _:
            raise Exception("BinaryOperator or UnaryOperator expected")


def fmt_operation(
    values: tuple[float, ...],
    operator: Operator,
    result: float | str,
    opts: dict[str, Any],
) -> str:
    fmt = get_formatter(opts)
    result = fmt(result) if isinstance(result, float) else result
    op_symbol = get_symbol(operator)

    match operator:
        case BinaryOperator():
            if len(values) != 2:
                raise Exception("Expected 2 values")

            left, right = values

            left_str = fmt(left)
            right_str = fmt(right)

            return f"{left_str} {op_symbol} {right_str} = {result}"

        case UnaryOperator():
            if len(values) != 1:
                raise Exception("Expected single value")

            value = fmt(values[0])
            return f"{op_symbol} {value} = {result}"
        case _:
            raise Exception("Invalid operator")
