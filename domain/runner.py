import logging
from dataclasses import dataclass

from domain.action import ActionCallable, Config, State, request_action
from std.repeat import repeat_while_requested


class AppBase:
    """
    Represents an abstraction of application with config, actions and state

    Attirbutes:
    config  Configuration options of application
    actions A list of actions, which can be performed
    state   An application state
    """

    config: Config
    actions: list[ActionCallable]
    state: State

    def __init__(self, config: Config, actions: list[ActionCallable]):
        self.config = config
        self.actions = actions
        self.state: State = None

    def perform_action(self, action: ActionCallable):
        logging.debug("App state before action")
        logging.debug(self.state)

        action(config=self.config, state=self.state)

        logging.debug("App state after action")
        logging.debug(self.state)


@dataclass
class RunnerOptions:
    """
    Represents the options of Runner class

    Attirbutes:

    continue_prompt_enabled Indicates whether to ask the user for continuation
    repeat                  Indicates whether to continue running, if first action is performed
    """

    continue_prompt_enabled: bool = True
    repeat: bool = True


class Runner:
    """
    Represents an application runner

    Attributes:

    app     An application to run
    options RunnerOptions instance
    """

    app: AppBase
    options: RunnerOptions

    def __init__(self, app: AppBase, options: RunnerOptions = RunnerOptions()):
        self.app = app
        self.options = options
        logging.debug("Runner spawned with options")
        logging.debug(self.options)

    def run_thread(self) -> None:
        action = request_action(self.app.actions)
        self.app.perform_action(action=action)

    def run(self) -> None:
        logging.debug("Runner running...")
        if self.options.repeat and self.options.continue_prompt_enabled:
            repeat_while_requested(action=self.run_thread)
        elif self.options.repeat:
            while True:
                self.run_thread()
        else:
            self.run_thread()

        logging.debug("Runner stopped")
