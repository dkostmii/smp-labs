from os import get_terminal_size

from lab4.domain.config import Config
from lab4.domain.state import AppState
from lab4.domain.term_color import InvalidColor, fore, style
from lab4.domain.text_renderer import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from std.read import (
    input_wrapper,
    read_single_float,
    read_single_int,
    read_until_pred,
    read_until_pred_custom,
)


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


def font_size_action(_: Config, state: AppState):
    font_size = read_until_pred_custom(
        custom_src=read_single_int,
        pred=lambda value: value > 0,
        title="Enter font size (must be positive)",
        invalid_msg="Font size must be positive",
    )

    state.font_size = font_size


def width_factor_action(_: Config, state: AppState):
    width_factor = read_until_pred_custom(
        custom_src=read_single_float,
        pred=lambda value: 0.5 <= value <= 2,
        title="Enter font width factor [0.5-2]",
        invalid_msg="Font width factor must be in range 0.5-2",
    )

    state.width_factor = width_factor


def stroke_width_action(_: Config, state: AppState):
    stroke_width = read_until_pred_custom(
        custom_src=read_single_float,
        pred=lambda value: 0.25 <= value <= 20,
        title="Enter stroke width [0.25-20]",
        invalid_msg="Font width factor must be in range 0.25-20",
    )

    state.stroke_width = stroke_width


def gap_action(_: Config, state: AppState):
    gap = read_until_pred_custom(
        custom_src=read_single_int,
        pred=lambda value: 0 <= value,
        title="Enter gap size (must be non-negative)",
        invalid_msg="Gap size must non-negative",
    )

    state.gap = gap


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
