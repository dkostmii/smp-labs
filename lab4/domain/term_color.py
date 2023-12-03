# Source: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal


class InvalidColor(Exception):
    def __init__(self, color):
        super().__init__(f"Invalid color: {color}")


def fore(color_name: str) -> str:
    if color_name == "red":
        return "\033[31m"
    elif color_name == "green":
        return "\033[32m"
    elif color_name == "blue":
        return "\033[34m"

    raise InvalidColor(color_name)


def style(style_name: str) -> str:
    if style_name == "reset":
        return "\033[0m"

    return ""
