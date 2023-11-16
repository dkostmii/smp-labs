from domain.action import ActionCallable, Action, AggregateAction
from runner import Runner, RunnerOptions, AppBase
from lab1.main import main as lab1_main
from lab2.main import main as lab2_main
from lab3.main import main as lab3_main
from lab4.main import main as lab4_main


class MainApp(AppBase):
    def __init__(self, actions: list[ActionCallable]):
        super().__init__(config=None, actions=actions)
        self.state = None


def main():
    app = MainApp(actions=[
        Action(name="Lab 1", action_fn=lambda _, __: lab1_main()),
        Action(name="Lab 2", action_fn=lambda _, __: lab2_main()),
        Action(name="Lab 3", action_fn=lambda _, __: lab3_main()),
        Action(name="Lab 4", action_fn=lambda _, __: lab4_main()),
    ])

    runner = Runner(app=app, options=RunnerOptions(repeat=False))
    runner.run()


if __name__ == "__main__":
    main()
