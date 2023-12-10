from os import get_terminal_size

from domain.term_color import fore, style

from .font_dict import get_font_dict
from .state import AppState
from .text_renderer import TextRenderer, TextRendererOptions


def render(state: AppState) -> str:
    term_size = get_terminal_size()
    (term_width, term_height) = (term_size.columns, term_size.lines)

    (width, height) = (
        state.size[0] if state.size[0] > 0 else term_width,
        state.size[1] if state.size[1] > 0 else term_height,
    )

    color = fore(state.color) if len(state.color) > 0 else ""

    font_dict = get_font_dict()

    options = TextRendererOptions(
        width=width,
        height=height,
        glyph_height=state.font_size,
        glyph_width_factor=state.width_factor,
        font_dict=font_dict,
        alignment=state.alignment,
        symbol=state.symbol,
        stroke_width=state.stroke_width,
        gap=state.gap,
    )

    renderer = TextRenderer(options)

    rendered_text = renderer.render(text=state.text)

    if len(state.color) > 0:
        rendered_text = f"{color}{rendered_text}{style('reset')}"

    return rendered_text
