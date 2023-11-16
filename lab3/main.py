from lab3.actions import actions
from lab3.config import read_config
from lab3.domain.app import App
from runner import Runner
from lab3.domain.config import Config


def main():
    config_data = read_config()
    config = Config(config_data=config_data)
    app = App(config=config, actions=actions)
    runner = Runner(app=app)
    runner.run()


if __name__ == "__main__":
    main()
