from config.opts import read_opts
from domain.action import Action
from domain.state import CalculatorState
from std.read import read_choose_from_list
from std.repeat import repeat_while_requested


class Calculator:
    def __init__(self, actions: list[Action]):
        self.actions = actions
        self.state = CalculatorState()

    def perform_action(self, action: Action):
        config_opts = read_opts()
        action(opts=config_opts, state=self.state)


def fmt_action(action: Action) -> str:
    return action.name


def request_action(action_list: list[Action]) -> Action:
    return read_choose_from_list(
        options=action_list, title="Choose operation:", formatter=fmt_action
    )


class Runner:
    def __init__(self, calculator: Calculator):
        self.calculator = calculator
        pass

    def run_thread(self) -> None:
        action = request_action(self.calculator.actions)
        self.calculator.perform_action(action=action)

    def run(self) -> None:
        repeat_while_requested(action=self.run_thread)
