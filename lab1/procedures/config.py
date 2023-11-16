from typing import Any

from lab1.config.defaults import defaults
from lab1.config.opts import parsers, validators, write_opts
from lab1.domain.state import CalculatorState
from std.read import read_choose_from_list, read_until_pred


def change_config_proc(opts: dict[str, Any], _: CalculatorState) -> None:
    print("Current config:")

    for i, key in enumerate(opts.keys()):
        print(f"{i + 1}. {key} => {opts[key]}")

    print()

    available_opts = list(defaults.keys())
    chosen_opt = read_choose_from_list(
        available_opts, "Choose config option to change: "
    )

    validate = validators[chosen_opt]
    parse = parsers[chosen_opt]

    val = read_until_pred(
        pred=validate,
        title=f"Enter a value for {chosen_opt}: ",
        invalid_msg=f"Enter a valid value for {chosen_opt}: ",
    )

    opts[chosen_opt] = parse(val)
    write_opts(opts)
