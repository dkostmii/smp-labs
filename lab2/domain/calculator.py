from lab2.config.opts import read_opts
from domain.action import Action
from lab2.domain.state import CalculatorState
from domain.action import ActionCallable
from runner import AppBase


class Calculator(AppBase):
    def __init__(self, actions: list[ActionCallable]):
        super().__init__(config=read_opts(), actions=actions)
        self.state = CalculatorState()

    def perform_action(self, action: Action):
        config_opts = read_opts()
        action(config=config_opts, state=self.state)
