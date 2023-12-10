from dataclasses import dataclass

from domain.action import ActionCallable, Config, State, request_action
from std.repeat import repeat_while_requested


class AppBase:
    def __init__(self, config: Config, actions: list[ActionCallable]):
        self.config = config
        self.actions = actions
        self.state: State = None

    def perform_action(self, action: ActionCallable):
        action(config=self.config, state=self.state)


@dataclass
class RunnerOptions:
    continue_prompt_enabled: bool = True
    repeat: bool = True


class Runner:
    def __init__(self, app: AppBase, options: RunnerOptions = RunnerOptions()):
        self.app = app
        self.options = options

    def run_thread(self) -> None:
        action = request_action(self.app.actions)
        self.app.perform_action(action=action)

    def run(self) -> None:
        if self.options.repeat and self.options.continue_prompt_enabled:
            repeat_while_requested(action=self.run_thread)
        elif self.options.repeat:
            while True:
                self.run_thread()
        else:
            self.run_thread()
