from domain.action import ActionCallable
from domain.runner import AppBase

from .config import Config
from .state import AppState, init_state


class App(AppBase):
    def __init__(self, config: Config, actions: list[ActionCallable]):
        super().__init__(config, actions)
        self.state = init_state(state=AppState(), config=self.config)
