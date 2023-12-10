from domain.runner import Runner, RunnerOptions

from .actions import actions
from .domain.calculator import Calculator


def main():
    calculator = Calculator(actions=actions)
    runner = Runner(
        app=calculator, options=RunnerOptions(continue_prompt_enabled=False)
    )
    runner.run()


if __name__ == "__main__":
    main()
