from domain.action import Action, AggregateAction

from .exit_action import exit_action
from .options import (
    camera_angle_action,
    camera_display_surface_action,
    camera_position_action,
    object_type_action,
    set_object_size_action,
    set_size_action,
    stroke_width_action,
    symbol_action,
    text_alignment_action,
    text_color_action,
)
from .preview_action import preview_action
from .save_action import save_action

actions = [
    Action(name="Specify object type", action_fn=object_type_action),
    AggregateAction(
        name="Options",
        actions=[
            Action(name="Choose text color", action_fn=text_color_action),
            Action(name="Set art size", action_fn=set_size_action),
            Action(name="Set object size", action_fn=set_object_size_action),
            Action(name="Set art symbol", action_fn=symbol_action),
            Action(name="Set text alignment", action_fn=text_alignment_action),
            Action(name="Set stroke width", action_fn=stroke_width_action),
            AggregateAction(
                name="Configure 3D projection",
                actions=[
                    Action(
                        name="Set camera position", action_fn=camera_position_action
                    ),
                    Action(name="Set camera angle", action_fn=camera_angle_action),
                    Action(
                        name="Set display surface position (relative to camera pinhole)",
                        action_fn=camera_display_surface_action,
                    ),
                ],
            ),
        ],
    ),
    Action(name="Preview art", action_fn=preview_action),
    Action(name="Save art to a file", action_fn=save_action),
    Action(name="Exit", action_fn=exit_action),
]

__all__ = ["actions"]
