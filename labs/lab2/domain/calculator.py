from domain.action import ActionCallable
from domain.runner import AppBase
from labs.lab2.config.opts import read_opts

from .state import CalculatorState


class Calculator(AppBase):
    def __init__(self, actions: list[ActionCallable]):
        super().__init__(config=read_opts("config/.calcrc.json"), actions=actions)
        self.state = CalculatorState()

    def perform_action(self, action: ActionCallable):
        config_opts = read_opts("config/.calcrc.json")
        action(config=config_opts, state=self.state)
