from actions.exit_action import exit_action
from actions.input_action import input_action
from actions.options import (font_action, set_size_action, symbol_action,
                             text_color_action)
from actions.preview_action import preview_action
from actions.save_action import save_action
from config import read_config
from domain.action import Action, AggregateAction
from domain.app import App, Runner
from domain.config import Config

actions = [
    AggregateAction(
        name="Options",
        actions=[
            Action(name="Choose font", action_fn=font_action),
            Action(name="Choose text color", action_fn=text_color_action),
            Action(name="Set art size", action_fn=set_size_action),
            Action(name="Set art symbol", action_fn=symbol_action),
        ],
    ),
    Action(name="Enter a text", action_fn=input_action),
    Action(name="Preview art", action_fn=preview_action),
    Action(name="Save art to a file", action_fn=save_action),
    Action(name="Exit", action_fn=exit_action),
]


def main():
    config_data = read_config()
    config = Config(config_data=config_data)
    app = App(config=config, actions=actions)
    runner = Runner(app=app)
    runner.run()


if __name__ == "__main__":
    main()
