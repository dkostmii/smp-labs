import json
from os.path import exists
from typing import Any, Callable

from config.defaults import defaults

validators: dict[str, Callable[[Any], bool]] = {
    "decimals": lambda x: x > -1,
    "history_count": lambda x: x > -1,
}


def validate_opts(opts: dict[str, Any]) -> None:
    for key in opts:
        if key not in defaults:
            raise Exception(f"Invalid config option: {key}")

        validator = validators[key]
        value = opts[key]
        is_valid = validator(value)

        if not is_valid:
            raise Exception(
                f"Invalid config value for key {key}. The value is: ${value}"
            )


def read_opts(config_file: str = ".calcrc.json") -> dict[str, Any]:
    if not exists(config_file):
        write_opts(defaults)

    with open(config_file, "r") as f:
        opts = json.load(f)
        merged = {**defaults, **opts}

        return merged


def write_opts(opts: dict[str, Any], config_file: str = ".calcrc.json") -> None:
    merged = {**defaults, **opts}
    validate_opts(merged)

    with open(config_file, "w") as f:
        json.dump(merged, f)
