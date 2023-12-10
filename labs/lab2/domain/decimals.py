from typing import Any, Callable


def get_formatter(opts: dict[str, Any]) -> Callable[[float], str]:
    def fmt(x: float):
        return ("{:." + str(int(opts["decimals"])) + "f}").format(x)

    if opts["decimals"] > 0:
        return fmt

    return lambda x: str(x)
