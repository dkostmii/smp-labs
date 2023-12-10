from domain.action import Action, AggregateAction

from .exit_action import exit_action
from .input_action import input_action
from .options import (font_action, set_size_action, symbol_action,
                      text_color_action)
from .preview_action import preview_action
from .save_action import save_action

actions = [
    AggregateAction(
        name="Options",
        actions=[
            Action(name="Choose font", action_fn=font_action),
            Action(name="Choose text color", action_fn=text_color_action),
            Action(name="Set art size", action_fn=set_size_action),
            Action(name="Set art symbol", action_fn=symbol_action),
        ],
    ),
    Action(name="Enter a text", action_fn=input_action),
    Action(name="Preview art", action_fn=preview_action),
    Action(name="Save art to a file", action_fn=save_action),
    Action(name="Exit", action_fn=exit_action),
]

__all__ = ["actions"]
