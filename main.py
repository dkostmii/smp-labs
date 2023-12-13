import logging

from domain.action import Action, ActionCallable, AggregateAction
from domain.logging import init_logging
from domain.runner import AppBase, Runner, RunnerOptions
from labs.lab1.main import main as lab1_main
from labs.lab2.main import main as lab2_main
from labs.lab3.main import main as lab3_main
from labs.lab4.main import main as lab4_main
from labs.lab5.main import main as lab5_main
from labs.lab6.main import main as lab6_main
from labs.lab7.main import main as lab7_main
from labs.lab7.tests.main import main as lab7_tests_main
from labs.lab8.main import main as lab8_main


class MainApp(AppBase):
    def __init__(self, actions: list[ActionCallable]):
        super().__init__(config=None, actions=actions)
        self.state = None


def main():
    init_logging()
    logging.info("Application starting...")

    try:
        app = MainApp(
            actions=[
                Action(name="Lab 1", action_fn=lambda *_: lab1_main()),
                Action(name="Lab 2", action_fn=lambda *_: lab2_main()),
                Action(name="Lab 3", action_fn=lambda *_: lab3_main()),
                Action(name="Lab 4", action_fn=lambda *_: lab4_main()),
                Action(name="Lab 5", action_fn=lambda *_: lab5_main()),
                Action(name="Lab 6", action_fn=lambda *_: lab6_main()),
                AggregateAction(
                    name="Lab 7",
                    actions=[
                        Action(name="App", action_fn=lambda *_: lab7_main()),
                        Action(name="Tests", action_fn=lambda *_: lab7_tests_main()),
                    ],
                ),
                Action(name="Lab 8", action_fn=lambda *_: lab8_main()),
            ]
        )

        runner = Runner(app=app, options=RunnerOptions(repeat=False))
        runner.run()

        logging.info("Application stopped")
    except Exception as e:
        logging.critical("Unhandled exception while running application")
        logging.critical(e)


if __name__ == "__main__":
    main()
