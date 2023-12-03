from os import get_terminal_size

from lab5.domain.object_dict import get_object_dict
from lab5.domain.object_renderer import ObjectRenderer, ObjectRendererOptions
from lab5.domain.state import AppState
from lab5.domain.term_color import fore, style


def render(state: AppState) -> str:
    term_size = get_terminal_size()
    (term_width, term_height) = (term_size.columns, term_size.lines)

    (width, height) = (
        state.size[0] if state.size[0] > 0 else term_width,
        state.size[1] if state.size[1] > 0 else term_height,
    )

    (object_width, object_height) = (
        state.object_size[0] if state.object_size[0] > 0 else width,
        state.object_size[1] if state.object_size[1] > 0 else height,
    )

    color = fore(state.color) if len(state.color) > 0 else ""

    object_dict = get_object_dict()

    options = ObjectRendererOptions(
        width=width,
        height=height,
        object_width=object_width,
        object_height=object_height,
        object_dict=object_dict,
        alignment=state.alignment,
        symbol=state.symbol,
        stroke_width=state.stroke_width,
        projection_params=state.projection_params,
    )

    renderer = ObjectRenderer(options)

    rendered_text = renderer.render(object_type=state.object_type)

    if len(state.color) > 0:
        rendered_text = f"{color}{rendered_text}{style('reset')}"

    return rendered_text
