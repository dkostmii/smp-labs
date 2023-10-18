from math import ceil, floor
from os import get_terminal_size
from re import sub

from colored import fore, style
from pyfiglet import Figlet

from domain.state import AppState
from std.str_ext import pad_bottom, pad_left, pad_top


def render(state: AppState) -> str:
    term_size = get_terminal_size()
    (term_width, term_height) = (term_size.columns, term_size.lines)

    (width, height) = (
        state.size[0] if state.size[0] > 0 else term_width,
        state.size[1] if state.size[1] > 0 else term_height,
    )

    color = fore(state.color) if len(state.color) > 0 else ""

    f = Figlet(font=state.font_name, width=width)
    rendered_text = f.renderText(text=state.text)

    if len(state.symbol) > 0:
        rendered_text = sub(r"[^\s]", state.symbol[0], rendered_text)

    if len(state.color) > 0:
        rendered_text = f"{color}{rendered_text}{style('reset')}"

    rendered_text_lines = list(
        filter(lambda line: len(line) > 0, rendered_text.split("\n"))
    )
    max_line_width = max([len(line) for line in rendered_text_lines])
    padding_left_size = ceil((width - max_line_width) / 2)

    if padding_left_size > 0:
        rendered_text_lines = [
            pad_left(text=line, count=padding_left_size) for line in rendered_text_lines
        ]

    rendered_text_height = len(rendered_text_lines)
    half_height_diff = (height - rendered_text_height) / 2
    padding_top_size = floor(half_height_diff)
    padding_bottom_size = ceil(half_height_diff)

    rendered_text = "\n".join(rendered_text_lines)

    if padding_top_size > 0:
        rendered_text = pad_top(text=rendered_text, count=padding_top_size)

    if padding_bottom_size > 0:
        rendered_text = pad_bottom(text=rendered_text, count=padding_bottom_size)

    return rendered_text
