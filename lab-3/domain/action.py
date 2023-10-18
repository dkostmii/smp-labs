from typing import Callable

from domain.config import Config
from domain.state import AppState
from std.read import read_choose_from_list

ActionFn = Callable[[Config, AppState], None]


class ActionCallable:
    def __init__(self):
        raise Exception("Attmept to create interface instance")

    def __call__(self, config: Config, state: AppState):
        raise Exception("Attempt to call interface instance")


class Action(ActionCallable):
    def __init__(self, name: str, action_fn: ActionFn):
        self.name = name
        self.action_fn = action_fn

    def __call__(self, config: Config, state: AppState) -> None:
        self.action_fn(config, state)


def fmt_action(action: Action) -> str:
    return action.name


def request_action(action_list: list[ActionCallable]) -> ActionCallable:
    return read_choose_from_list(
        options=action_list, title="Choose operation:", formatter=fmt_action
    )


class AggregateAction(ActionCallable):
    name: str
    actions: list[ActionCallable]

    def __init__(self, name: str, actions: list[ActionCallable]):
        self.name = name
        self.actions = actions

    def __call__(self, config: Config, state: AppState) -> None:
        action = request_action(self.actions)
        action(config, state)
