from labs.lab7.domain.config import Config
from labs.lab7.domain.state import AppState


def history_action(_: Config, state: AppState):
    if len(state.history) == 0:
        print("No history!")
    else:
        for counter, item in enumerate(state.history):
            print(f"{counter + 1}: {item}")
