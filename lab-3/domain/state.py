from domain.config import Config


class AppState:
    text: str
    color: str
    font_name: str
    size: tuple[int, int]
    symbol: str

    def __init__(self):
        self.text = ""
        self.color = ""
        self.font_name = ""
        self.size = (-1, -1)
        self.symbol = ""


def init_state(state: AppState, config: Config) -> AppState:
    state.text = config.text.default
    state.font_name = config.fonts[0]

    return state
