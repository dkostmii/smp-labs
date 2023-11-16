from math import ceil, floor
from os import get_terminal_size
from re import sub

from lab4.domain.state import AppState
from lab4.domain.text_renderer import TextRenderer, TextRendererOptions
from lab4.domain.term_color import fore, style
from std.str_ext import pad_bottom, pad_left, pad_top

import json


def render(state: AppState) -> str:
    term_size = get_terminal_size()
    (term_width, term_height) = (term_size.columns, term_size.lines)

    (width, height) = (
        state.size[0] if state.size[0] > 0 else term_width,
        state.size[1] if state.size[1] > 0 else term_height,
    )

    color = fore(state.color) if len(state.color) > 0 else ""

    with open("lab4/data/fonts.json", mode="r", encoding="utf-8") as f:
        font_dict: dict[str, list[Point]] = json.load(f)

    options = TextRendererOptions(
        width=width,
        height=height,
        glyph_height=state.font_size,
        glyph_width_factor=state.width_factor,
        font_dict=font_dict,
        alignment=state.alignment,
        symbol=state.symbol,
        stroke_width=2,
        gap=2
    )

    renderer = TextRenderer(options)

    rendered_text = renderer.render(text=state.text)

    if len(state.color) > 0:
        rendered_text = f"{color}{rendered_text}{style('reset')}"

    return rendered_text
