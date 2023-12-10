from math import sqrt
from typing import Callable

from std.result import Err, Ok, Result


class Operator:
    def __init__(self, evaluator: Callable[..., float | Result]):
        self.evaluator = evaluator


class BinaryOperator(Operator):
    evaluator: Callable[[float, float], float | Result]

    def __init__(self, evaluator: Callable[[float, float], float | Result]):
        super().__init__(evaluator)

    def apply(self, left: float, right: float) -> float | Result:
        return self.evaluator(left, right)


class UnaryOperator(Operator):
    evaluator: Callable[[float], float | Result]

    def __init__(self, evaluator: Callable[[float], float | Result]):
        super().__init__(evaluator)

    def apply(self, x: float) -> float | Result:
        return self.evaluator(x)


operators: dict[str, Operator] = {
    "+": BinaryOperator(evaluator=lambda left, right: left + right),
    "-": BinaryOperator(evaluator=lambda left, right: left - right),
    "*": BinaryOperator(evaluator=lambda left, right: left * right),
    "/": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left / right))
        if right != 0
        else Result(Err(val="Cannot divide by zero."))
    ),
    "^": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left**right))
        if not (left == right == 0)
        else Result(Err(val=f"{left}^{right} is undefined."))
    ),
    "sqrt": UnaryOperator(
        evaluator=lambda x: Result(Ok(sqrt(x)))
        if x >= 0
        else Result(Err(val="Square root is not defined for negative numbers."))
    ),
    "%": BinaryOperator(
        evaluator=lambda left, right: Result(Ok(left % right))
        if right != 0
        else Result(Err(val="Cannot divide by zero."))
    ),
}


def get_symbol(operator: Operator) -> str | None:
    return next(filter(lambda symbol: operators[symbol] == operator, operators))


def get_operator(symbol: str) -> Operator | None:
    return operators[symbol]
