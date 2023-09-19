from std.result import Result, Ok, Err
from calc import CalculatorState
from std.read import read_until_pred, read_single_num, read_yes_no
from math import sqrt
from typing import Callable, Any

from calc import HistoryEntry


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


def read_num_or_memory(state: CalculatorState, title: str = "") -> float:

    if state.has_in_memory():
        confirmed = read_yes_no(f"The memory contains value [{state.memory[-1]}]. Do you want to use that value?", default=False)

        if confirmed:
            return state.get_memory()

    return read_single_num(title)



def read_nums(op: Operator, state: CalculatorState) -> tuple[float,...]:
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


def read_op(state: CalculatorState) -> tuple[Operator, tuple[float,...]]:
    valid_ops = list(ops.keys())
    valid_ops_str = ", ".join(valid_ops)

    op_key = read_until_pred(lambda x: x in valid_ops, f"Choose an operation [{valid_ops_str}]: ", "Invalid operator. Try again")
    op = ops[op_key]

    values = read_nums(op, state)

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


def get_formatter(opts: dict[str, Any]) -> Callable[[float], str]:
    def fmt(x: float):
        return ("{:." + str(int(opts["decimals"])) + "f}").format(x)

    if opts["decimals"] > 0:
        return fmt

    return lambda x: str(x)


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


def get_op_sign(op: Operator) -> str:
    for key in ops:
        if ops[key] == op:
            return key

    raise Exception("Unknown op")


def get_operation_str(op: Operator, values: list[float], opts: dict[str, Any]) -> str:
    fmt = get_formatter(opts)

    str_values: list[str] = [fmt(values[0])]

    if len(values) > 1:
        str_values.append(fmt(values[1]))

    match op:
        case UnaryOperator():
            return get_op_sign(op) + "(" + str_values[0] + ")"
        case BinaryOperator():
            return str_values[0] + " " + get_op_sign(op) + " " + str_values[1]


def do_calculation_proc(opts: dict[str, Any], state: CalculatorState) -> None:
    op, values = read_op(state)
    op_res = apply_op(op, values)

    entry_res = None

    match op_res:
        case float():
            entry_res = op_res
        case Result(is_ok=True):
            if op_res.ok_val is None:
                raise Exception("Expected op_res.ok_val")
            entry_res = op_res.ok_val.val
        case _:
            entry_res = None

    entry = HistoryEntry(get_operation_str(op, list(values), opts), entry_res)
    state.add_history_entry(entry, opts)

    display_op_res(op_res, opts)
