from lab5.actions import actions
from lab5.config import read_config
from lab5.domain.app import App, Runner
from lab5.domain.config import Config


def main():
    config_data = read_config()
    config = Config(config_data=config_data)
    app = App(config=config, actions=actions)
    runner = Runner(app=app)
    runner.run()


if __name__ == "__main__":
    main()
