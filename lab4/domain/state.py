from lab4.domain.config import Config
from lab4.domain.types import Size
from lab4.domain.text_renderer import ALIGN_LEFT


class AppState:
    text: str
    color: str
    size: Size
    width_factor: float
    font_size: int
    stroke_width: float
    symbol: str
    alignment: str

    def __init__(self):
        self.text = ""
        self.color = ""
        self.size = (-1, -1)
        self.width_factor = 1.0
        self.font_size = 5
        self.stroke_width = 1.0
        self.symbol = "@"
        self.alignment = ALIGN_LEFT


def init_state(state: AppState, config: Config) -> AppState:
    state.text = config.text.default

    return state
