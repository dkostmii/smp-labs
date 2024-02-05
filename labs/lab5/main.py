from domain.runner import Runner, RunnerOptions

from .actions import actions
from .domain.app import App
from .domain.config import Config


def main():
    app = App(config=Config(), actions=actions)
    runner = Runner(app=app, options=RunnerOptions(continue_prompt_enabled=False))
    runner.run()


if __name__ == "__main__":
    main()
