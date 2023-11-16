from lab4.actions.exit_action import exit_action
from lab4.actions.input_action import input_action
from lab4.actions.preview_action import preview_action
from lab4.actions.save_action import save_action

from lab4.actions.options import (
    text_color_action, set_size_action, symbol_action,
    text_alignment_action, font_size_action, width_factor_action,
    stroke_width_action, gap_action
)

from domain.action import AggregateAction, Action

actions = [
    AggregateAction(
        name="Options",
        actions=[
            Action(name="Choose text color", action_fn=text_color_action),
            Action(name="Set art size", action_fn=set_size_action),
            Action(name="Set art symbol", action_fn=symbol_action),
            Action(name="Set text alignment", action_fn=text_alignment_action),
            Action(name="Set font size", action_fn=font_size_action),
            Action(name="Set width factor", action_fn=width_factor_action),
            Action(name="Set stroke width", action_fn=stroke_width_action),
            Action(name="Set gap between letters", action_fn=gap_action),
        ],
    ),
    Action(name="Enter a text", action_fn=input_action),
    Action(name="Preview art", action_fn=preview_action),
    Action(name="Save art to a file", action_fn=save_action),
    Action(name="Exit", action_fn=exit_action),
]

__all__ = [
   "actions"
]
