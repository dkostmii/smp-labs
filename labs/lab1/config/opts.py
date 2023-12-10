import json
from os.path import exists
from typing import Any, Callable

from std.num_ext import try_parse_int

from .defaults import defaults


def uint_validator(value: str) -> bool:
    number = try_parse_int(value)
    return isinstance(number, int) and number > -1


validators: dict[str, Callable[[str], bool]] = {
    "decimals": uint_validator,
    "history_count": uint_validator,
}


parsers: dict[str, Callable[[str], Any]] = {
    "decimals": try_parse_int,
    "history_count": try_parse_int,
}


def validate_opts(opts: dict[str, Any]) -> None:
    for key in opts:
        if key not in defaults:
            raise Exception(f"Invalid config option: {key}")

        validate = validators[key]
        value = opts[key]
        is_valid = validate(value)

        if not is_valid:
            raise Exception(
                f"Invalid config value for key {key}. The value is: {value}"
            )


def read_opts(config_file: str = ".calcrc.json") -> dict[str, Any]:
    if not exists(config_file):
        write_opts(defaults)

    with open(config_file, "r") as f:
        opts = json.load(f)
        merged = {**defaults, **opts}
        validate_opts(merged)

        return merged


def write_opts(opts: dict[str, Any], config_file: str = ".calcrc.json") -> None:
    merged = {**defaults, **opts}
    validate_opts(merged)

    with open(config_file, "w") as f:
        json.dump(merged, f)
