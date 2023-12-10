from domain.runner import Runner, RunnerOptions
from helpers.ascii_config import read_config

from .actions import actions
from .domain.app import App
from .domain.config import Config


def main():
    config_data = read_config(config_file_path="config/lab5.json")
    config = Config(config_data=config_data)
    app = App(config=config, actions=actions)
    runner = Runner(app=app, options=RunnerOptions(continue_prompt_enabled=False))
    runner.run()


if __name__ == "__main__":
    main()
