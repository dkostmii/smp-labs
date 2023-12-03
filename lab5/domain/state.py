from lab5.domain.config import Config
from lab5.domain.object_dict import get_object_dict
from lab5.domain.object_renderer import ALIGN_LEFT, ProjectionParams
from lab5.domain.types import Size


class AppState:
    object_type: str
    color: str
    size: Size
    object_size: Size
    stroke_width: float
    symbol: str
    alignment: int
    projection_params: ProjectionParams

    def __init__(self):
        self.text = ""
        self.color = ""
        self.object_type = ""
        self.size = (-1, -1)
        self.object_size = (-1, -1)
        self.stroke_width = 1.0
        self.symbol = "@"
        self.alignment = ALIGN_LEFT
        self.projection_params = ProjectionParams(
            c=(0, 0, -1),
            theta=(0, 0, 0),
            e=(0, 0, 1),
        )


def init_state(state: AppState, config: Config) -> AppState:
    object_dict = get_object_dict()
    valid_object_types = list(object_dict.keys())
    state.object_type = valid_object_types[0]

    return state
