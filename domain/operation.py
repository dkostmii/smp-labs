from math import sqrt
from typing import Any, Callable

from std.result import Err, Ok, Result

from .decimals import get_formatter


class OperationError(Exception):
    message: str

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Operation error: {self.message}"

    @staticmethod
    def from_message(message: str):
        return OperationError(message.replace("Operation error: ", ""))


OperationResult = Result[float, OperationError]


class Operator:
    def __init__(self, evaluator: Callable[..., float | OperationResult]):
        self.evaluator = evaluator


class BinaryOperator(Operator):
    evaluator: Callable[[float, float], float | Result]

    def __init__(self, evaluator: Callable[[float, float], float | OperationResult]):
        super().__init__(evaluator)

    def apply(self, left: float, right: float) -> float | OperationResult:
        return self.evaluator(left, right)


class UnaryOperator(Operator):
    evaluator: Callable[[float], float | OperationResult]

    def __init__(self, evaluator: Callable[[float], float | OperationResult]):
        super().__init__(evaluator)

    def apply(self, x: float) -> float | OperationResult:
        return self.evaluator(x)


def apply_op(op: Operator, values: tuple[float, ...]) -> float | OperationResult:
    match op:
        case UnaryOperator():
            (x,) = values
            return op.apply(x)
        case BinaryOperator():
            (left, right) = values
            return op.apply(left, right)

        case _:
            raise Exception("BinaryOperator or UnaryOperator expected")


def get_symbol(operator: Operator) -> str | None:
    return next(filter(lambda symbol: operators[symbol] == operator, operators))


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


operators: dict[str, Operator] = {
    "+": BinaryOperator(evaluator=lambda left, right: left + right),
    "-": BinaryOperator(evaluator=lambda left, right: left - right),
    "*": BinaryOperator(evaluator=lambda left, right: left * right),
    "/": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left / right))
        if right != 0
        else Result(Err(val=OperationError("Cannot divide by zero.")))
    ),
    "^": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left**right))
        if not (left == right == 0)
        else Result(Err(val=OperationError(f"{left}^{right} is undefined.")))
    ),
    "sqrt": UnaryOperator(
        evaluator=lambda x: Result(Ok(sqrt(x)))
        if x >= 0
        else Result(
            Err(val=OperationError("Square root is not defined for negative numbers."))
        )
    ),
    "%": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left % right))
        if right != 0
        else Result(Err(val=OperationError("Cannot divide by zero.")))
    ),
}


def get_operator(symbol: str) -> Operator | None:
    return operators[symbol]
