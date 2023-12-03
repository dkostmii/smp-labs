from lab5.domain.config import Config
from lab5.domain.render import render
from lab5.domain.state import AppState


def preview_action(_: Config, state: AppState):
    render_result = render(state=state)
    print("Preview:")
    print(render_result)
    print()
