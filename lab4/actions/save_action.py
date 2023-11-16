from lab4.domain.config import Config
from lab4.domain.render import render
from lab4.domain.state import AppState
from std.read import read_filename


def save_action(_: Config, state: AppState):
    render_result = render(state=state)

    filename = read_filename(
        title="Enter a file name to save art to:", check_writable=True
    )

    with open(filename, mode="w") as f:
        f.write(render_result)

    print(f"Successfully saved art to {filename} file.")
    print()
