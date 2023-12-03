from domain.action import Action, ActionCallable
from lab2.actions.calc_action import calc_action
from lab2.actions.config_action import config_action
from lab2.actions.exit_action import exit_action
from lab2.actions.history_action import history_action
from lab2.actions.memory import clear_memory_action, save_to_memory_action

actions: list[ActionCallable] = [
    Action(name="Change config", action_fn=config_action),
    Action(name="Display history", action_fn=history_action),
    Action(name="Clear memory", action_fn=clear_memory_action),
    Action(name="Save to memory", action_fn=save_to_memory_action),
    Action(name="Do calculation", action_fn=calc_action),
    Action(name="Exit", action_fn=exit_action),
]

__all__ = ["actions"]
