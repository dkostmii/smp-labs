from domain.types import Size

from .config import Config
from .text_renderer import ALIGN_LEFT


class AppState:
    text: str
    color: str
    size: Size
    width_factor: float
    font_size: int
    stroke_width: float
    symbol: str
    alignment: int
    gap: int

    def __init__(self):
        self.text = ""
        self.color = ""
        self.size = (-1, -1)
        self.width_factor = 1.0
        self.font_size = 5
        self.stroke_width = 1.0
        self.symbol = "@"
        self.alignment = ALIGN_LEFT
        self.gap = 1


def init_state(state: AppState, config: Config) -> AppState:
    state.text = config.text.default

    return state
