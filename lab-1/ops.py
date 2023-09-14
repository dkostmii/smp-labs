from result import Result, Ok, Err
from read import read_until_pred, read_single_num
from math import sqrt
from typing import Callable


class BinaryOperator:
    def __init__(self, evaluator: Callable[[float, float], float | Result]):
        self.evaluator = evaluator

    def apply(self, left: float, right: float) -> float | Result:
        return self.evaluator(left, right)


class UnaryOperator:
    def __init__(self, evaluator: Callable[[float], float | Result]):
        self.evaluator = evaluator

    def apply(self, x) -> float | Result:
        return self.evaluator(x)


Operator = BinaryOperator | UnaryOperator


ops: dict[str, Operator] = {
    "+": BinaryOperator(evaluator=lambda left, right: left + right),
    "-": BinaryOperator(evaluator=lambda left, right: left - right),
    "*": BinaryOperator(evaluator=lambda left, right: left * right),
    "/": BinaryOperator(evaluator=lambda left, right: Result(Ok(left / right)) if right != 0 else Result(Err("Cannot divide by zero."))),
    "^": BinaryOperator(evaluator=lambda left, right: left ** right if not (left == right == 0) else Result(Err(f"{left}^{right} is undefined."))),
    "sqrt": UnaryOperator(evaluator=lambda x: sqrt(x) if x >= 0 else Result(Err("Square root is not defined for negative numbers."))),
    "%": BinaryOperator(evaluator=lambda left, right: Result(Ok(left % right)) if right != 0 else Result(Err("Cannot divide by zero."))),
}


def read_nums(op: Operator) -> tuple[float,...]:
    match op:
        case BinaryOperator():
            left = read_single_num("Enter a first number: ")
            right = read_single_num("Enter a second number: ")
            return (left, right)

        case UnaryOperator():
            x = read_single_num("Enter a number: ")
            return (x,)

        case _:
            raise Exception("BinaryOperator or UnaryOperator expected")


def read_op() -> tuple[Operator, tuple[float,...]]:
    valid_ops = list(ops.keys())
    valid_ops_str = ", ".join(valid_ops)

    op_key = read_until_pred(lambda x: x in valid_ops, f"Choose an operation [{valid_ops_str}]: ", "Invalid operator. Try again")
    op = ops[op_key]

    values = read_nums(op)

    return op, values


def apply_op(op: Operator, values: tuple[float,...]) -> float | Result:
    match op:
        case UnaryOperator():
            (x,) = values
            return op.apply(x)
        case BinaryOperator():
            (left, right) = values
            return op.apply(left, right)

        case _:
            raise Exception("BinaryOperator or UnaryOperator expected")


def display_err(err: Err) -> None:
    print(f"Error: {err.val}")


def display_val(val: Ok | float) -> None:
    match val:
        case Ok():
            return print(f"=> {val.val}")
        case float():
            return print(f"=> {val}")
        case _:
            raise ValueError("Ok or float expected")


def display_op_res(val: float | Result) -> None:
    match val:
        case Result():
            return val.map(display_val, display_err)
        case float():
            return display_val(val)
        case _:
            raise Exception("Expected Result or float")

