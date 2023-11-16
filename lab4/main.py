from lab4.config import read_config
from lab4.actions import actions
from domain.action import Action, AggregateAction
from lab4.domain.app import App, Runner
from lab4.domain.config import Config


def main():
    config_data = read_config()
    config = Config(config_data=config_data)
    app = App(config=config, actions=actions)
    runner = Runner(app=app)
    runner.run()


if __name__ == "__main__":
    main()
