from typing import Any, Callable

from domain.state import CalculatorState

ActionFn = Callable[[dict[str, Any], CalculatorState], None]


class Action:
    def __init__(self, name: str, action_fn: ActionFn):
        self.name = name
        self.action_fn = action_fn
        pass

    def __call__(self, opts: dict[str, Any], state: CalculatorState) -> None:
        self.action_fn(opts, state)
