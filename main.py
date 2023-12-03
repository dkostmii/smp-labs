from domain.action import Action, ActionCallable
from lab1.main import main as lab1_main
from lab2.main import main as lab2_main
from lab3.main import main as lab3_main
from lab4.main import main as lab4_main
from lab5.main import main as lab5_main
from lab6.main import main as lab6_main
from runner import AppBase, Runner, RunnerOptions


class MainApp(AppBase):
    def __init__(self, actions: list[ActionCallable]):
        super().__init__(config=None, actions=actions)
        self.state = None


def main():
    app = MainApp(
        actions=[
            Action(name="Lab 1", action_fn=lambda *_: lab1_main()),
            Action(name="Lab 2", action_fn=lambda *_: lab2_main()),
            Action(name="Lab 3", action_fn=lambda *_: lab3_main()),
            Action(name="Lab 4", action_fn=lambda *_: lab4_main()),
            Action(name="Lab 5", action_fn=lambda *_: lab5_main()),
            Action(name="Lab 6", action_fn=lambda *_: lab6_main()),
        ]
    )

    runner = Runner(app=app, options=RunnerOptions(repeat=False))
    runner.run()


if __name__ == "__main__":
    main()
