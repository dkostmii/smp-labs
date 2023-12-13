import logging
from typing import Any, Callable

from std.read import read_choose_from_list

Config = Any
State = Any
ActionFn = Callable[[Config, State], None]


class ActionCallable:
    """
    Represents an abstract action that is performed by runner.
    """

    def __init__(self):
        raise Exception("Attmept to create interface instance")

    def __call__(self, config: Config, state: State):
        raise Exception("Attempt to call interface instance")


class Action(ActionCallable):
    """
    Represents a single action that is performed by runner.

    Attributes:
    name      The name of the action displayed in UI
    action_fn A function to call to perform the action
    """

    name: str
    action_fn: ActionFn

    def __init__(self, name: str, action_fn: ActionFn):
        self.name = name
        self.action_fn = action_fn

    def __call__(self, config: Config, state: State) -> None:
        logging.debug(f"Performing '{self.name}' action...")
        self.action_fn(config, state)
        logging.debug(f"Done '{self.name}' action...")


def fmt_action(action: Action) -> str:
    return action.name


def request_action(action_list: list[ActionCallable]) -> ActionCallable:
    return read_choose_from_list(
        options=action_list, title="Choose operation:", formatter=fmt_action
    )


class AggregateAction(ActionCallable):
    """
    Represents an aggregate action that is performed by runner.

    Attributes:
    name      The name of the action displayed in UI
    actions   A list of actions to choose from
    """

    name: str
    actions: list[ActionCallable]

    def __init__(self, name: str, actions: list[ActionCallable]):
        self.name = name
        self.actions = actions

    def __call__(self, config: Config, state: State) -> None:
        logging.debug(f"Performing aggregate action '{self.name}'")
        action = request_action(self.actions)
        action(config, state)
        logging.debug(f"Done aggregate action '{self.name}'")
