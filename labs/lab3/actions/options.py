from os import get_terminal_size

from colored import Colored, fore, style
from colored.exceptions import InvalidColor, InvalidHexColor

from labs.lab3.domain.config import Config
from labs.lab3.domain.state import AppState
from std.read import (input_wrapper, read_choose_from_list, read_single_int,
                      read_until_pred, read_until_pred_custom)


def font_action(config: Config, state: AppState):
    print(f"Current font: {state.font_name}")

    font = read_choose_from_list(options=config.fonts, title="Choose a font: ")
    state.font_name = font

    print(f"Changed font to {font}")


def text_color_action(_: Config, state: AppState):
    if not Colored.enabled():
        print("Coloring is not supported by this terminal.")
        return

    invalid = True

    if len(state.color) > 0:
        print(f"Current color: {fore(state.color)}{state.color}{style('reset')}")

    while invalid:
        color_input = input_wrapper(
            "Enter a color [name or HEX or empty for no color]: "
        )

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
        except InvalidHexColor:
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
    print(f"Changed width to {state.size[0]}")
    print(f"Changed width to {state.size[1]}")


def symbol_action(config: Config, state: AppState):
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
