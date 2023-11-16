from lab3.domain.config import Config
from lab3.domain.state import AppState
from std.read import read_until_pred


def input_action(config: Config, state: AppState):
    prev_text = state.text if len(state.text) > 0 else config.text.default
    print(f"Current text: {prev_text}")

    text = read_until_pred(
        pred=lambda t: 0 < len(t) < config.text.max_length,
        title="Enter text to make art from: ",
        invalid_msg=f"Expected text with length at least 1 and at most {config.text.max_length}",
    )

    state.text = text[: config.text.max_length]
    print(f"Changed text to {state.text}")
