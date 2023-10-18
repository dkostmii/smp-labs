from domain.action import ActionCallable, request_action
from domain.config import Config
from domain.state import AppState, init_state


class App:
    def __init__(self, config: Config, actions: list[ActionCallable]):
        self.config = config
        self.actions = actions
        self.state = init_state(state=AppState(), config=self.config)

    def perform_action(self, action: ActionCallable):
        action(config=self.config, state=self.state)


class Runner:
    def __init__(self, app: App):
        self.app = app
        pass

    def run_thread(self) -> None:
        action = request_action(self.app.actions)
        self.app.perform_action(action=action)

    def run(self) -> None:
        while True:
            self.run_thread()
