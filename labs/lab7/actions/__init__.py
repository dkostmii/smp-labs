from actions.exit_action import exit_action
from domain.action import Action, ActionCallable

from .display_action import display_action
from .history_action import history_action
from .save_file_action import save_file_action

actions: list[ActionCallable] = [
    Action(name="Get user info", action_fn=display_action),
    Action(name="Display history", action_fn=history_action),
    Action(name="Save last result to a file", action_fn=save_file_action),
    Action(name="Exit", action_fn=exit_action),
]

__all__ = ["actions"]
