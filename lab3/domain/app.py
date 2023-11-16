from domain.action import ActionCallable
from lab3.domain.config import Config
from lab3.domain.state import AppState, init_state
from runner import AppBase


class App(AppBase):
    def __init__(self, config: Config, actions: list[ActionCallable]):
        super().__init__(config, actions)
        self.state = init_state(state=AppState(), config=self.config)
