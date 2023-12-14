from math import pi
from os import get_terminal_size

from domain.geometry import get_3d_dist
from domain.term_color import InvalidColor, fore, style
from domain.types import Angle3F, Point3F
from labs.lab5.domain.config import Config
from labs.lab5.domain.object_dict import get_object_dict
from labs.lab5.domain.object_renderer import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from labs.lab5.domain.state import AppState
from std.read import (
    input_wrapper,
    read_list_of,
    read_single_float,
    read_single_int,
    read_until_pred,
    read_until_pred_custom,
)


def object_type_action(_: Config, state: AppState):
    object_dict = get_object_dict()

    valid_object_types = list(object_dict.keys())

    object_type = read_until_pred(
        pred=lambda t: t in valid_object_types,
        title=f"Choose an object type [{', '.join(valid_object_types)}]",
        invalid_msg="Invalid object type.",
    )

    state.object_type = object_type


def text_alignment_action(_: Config, state: AppState):
    alignment_name = read_until_pred(
        pred=lambda name: name.lower() in ["left", "center", "right"],
        title="How to align a text? [left, center, right]",
        invalid_msg="Alignment must be left, center or right",
    )

    if alignment_name == "left":
        state.alignment = ALIGN_LEFT
    elif alignment_name == "center":
        state.alignment = ALIGN_CENTER
    elif alignment_name == "right":
        state.alignment = ALIGN_RIGHT
    else:
        raise Exception("Invalid alignment value.")


def camera_position_action(_: Config, state: AppState):
    camera_pos: list[float] = read_list_of(
        custom_src=read_single_float,
        repeat_pred=lambda values: len(values) == 3,
        pred=lambda values: get_3d_dist(tuple(values), state.projection_params.e) != 0,
        title="Enter camera position",
        invalid_msg="Expected non-zero camera pinhole to display surface distance",
    )

    if len(camera_pos) < 3:
        raise Exception("Expected camera_pos to have at least 3 items")

    c: Point3F = (camera_pos[0], camera_pos[1], camera_pos[2])
    state.projection_params.c = c


def camera_angle_action(_: Config, state: AppState):
    camera_angle: list[float] = read_list_of(
        custom_src=read_single_float,
        repeat_pred=lambda values: len(values) == 3,
        pred=lambda _: True,
        title="Enter camera angle (degrees)",
    )

    if len(camera_angle) < 3:
        raise Exception("Expected camera_angle to have at least 3 items")

    theta: Angle3F = (
        2 * pi * camera_angle[0] / 360,
        2 * pi * camera_angle[1] / 360,
        2 * pi * camera_angle[2] / 360,
    )

    state.projection_params.theta = theta


def camera_display_surface_action(_: Config, state: AppState):
    disp_surf_pos: list[float] = read_list_of(
        custom_src=read_single_float,
        repeat_pred=lambda values: len(values) == 3,
        pred=lambda values: get_3d_dist(tuple(values), state.projection_params.e) != 0,
        title="Enter display surface position (relative to the camera pinhole)",
        invalid_msg="Expected non-zero camera pinhole to display surface distance",
    )

    if len(disp_surf_pos) < 3:
        raise Exception("Expected disp_surf_pos to have at least 3 items")

    e: Point3F = (disp_surf_pos[0], disp_surf_pos[1], disp_surf_pos[2])
    state.projection_params.e = e


def stroke_width_action(_: Config, state: AppState):
    stroke_width = read_until_pred_custom(
        custom_src=read_single_float,
        pred=lambda value: 0.25 <= value <= 20,
        title="Enter stroke width [0.25-20]",
        invalid_msg="Font width factor must be in range 0.25-20",
    )

    state.stroke_width = stroke_width


def text_color_action(_: Config, state: AppState):
    invalid = True

    if len(state.color) > 0:
        print(f"Current color: {fore(state.color)}{state.color}{style('reset')}")

    while invalid:
        color_input = input_wrapper("Enter a color name [red, green or blue]: ")

        if len(color_input) < 1:
            state.color = ""
            invalid = False
            print("Changed color to no color")
            return

        try:
            color = fore(color_input.lower())
            state.color = color_input
            print(f"Changed color to {color}{color_input}{style('reset')}.")
            invalid = False

        except InvalidColor:
            print(f"Invalid color: {color_input}.")


def set_size_action(_: Config, state: AppState):
    term_size = get_terminal_size()
    (max_width, max_height) = (term_size.columns, term_size.lines)

    (current_width, current_height) = (
        state.size[0] if state.size[0] > 0 else max_width,
        state.size[1] if state.size[1] > 0 else max_height,
    )

    print(f"Current width: {current_width}")
    print(f"Current height: {current_height}")

    width = read_until_pred_custom(
        read_single_int,
        lambda v: -1 <= int(v) <= max_width,
        "Enter width: ",
        f"Invalid width. Expected width at least 1 and up to {max_width} or -1, 0 for default case.",
    )

    height = read_until_pred_custom(
        read_single_int,
        lambda v: -1 <= int(v) <= max_height,
        "Enter height: ",
        f"Invalid height. Expected height at least 1 and up to {max_height} or -1, 0 for default case.",
    )

    if width < 1:
        width = -1

    if height < 1:
        height = -1

    state.size = (width, height)
    print(
        f"Changed width to {state.size[0] if state.size[0] > 0 else '[default width]'}"
    )
    print(
        f"Changed height to {state.size[1] if state.size[1] > 0 else '[default height]'}"
    )


def set_object_size_action(_: Config, state: AppState):
    term_size = get_terminal_size()
    (max_width, max_height) = (term_size.columns, term_size.lines)

    if max_width > state.size[0] and state.size[0] > 0:
        max_width = state.size[0]

    if max_height > state.size[1] and state.size[1] > 0:
        max_height = state.size[1]

    (current_width, current_height) = (
        state.object_size[0] if state.object_size[0] > 0 else max_width,
        state.object_size[1] if state.object_size[1] > 0 else max_height,
    )

    print(f"Current object width: {current_width}")
    print(f"Current object height: {current_height}")

    object_width = read_until_pred_custom(
        read_single_int,
        lambda v: -1 <= int(v) <= max_width,
        "Enter object width: ",
        f"Invalid width. Expected width at least 1 and up to {max_width} or -1, 0 for default case.",
    )

    object_height = read_until_pred_custom(
        read_single_int,
        lambda v: -1 <= int(v) <= max_height,
        "Enter object height: ",
        f"Invalid height. Expected height at least 1 and up to {max_height} or -1, 0 for default case.",
    )

    if object_width < 1:
        object_width = -1

    if object_height < 1:
        object_height = -1

    state.object_size = (object_width, object_height)
    print(
        f"Changed object width to {state.object_size[0] if state.object_size[0] > 0 else '[default object width]'}"
    )
    print(
        f"Changed object height to {state.object_size[1] if state.object_size[1] > 0 else '[default object height]'}"
    )


def symbol_action(_: Config, state: AppState):
    if state.symbol:
        print(f"Current symbol: {state.symbol[0]}")

    symbol = read_until_pred(
        pred=lambda s: len(s) <= 1,
        title="Enter a symbol to draw art with (no symbol sets default symbol for a font): ",
        invalid_msg="Expect at most 1 symbol",
    )

    state.symbol = symbol

    symbol_caption = symbol if len(symbol) > 0 else "default symbol for a font"
    print(f"Changed symbol to {symbol_caption}")
