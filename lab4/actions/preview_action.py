from lab4.domain.config import Config
from lab4.domain.render import render
from lab4.domain.state import AppState


def preview_action(_: Config, state: AppState):
    render_result = render(state=state)
    print("Preview:")
    print(render_result)
    print()
