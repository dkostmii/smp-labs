from typing import Any

from labs.lab2.config.defaults import defaults
from labs.lab2.config.opts import parsers, validators, write_opts
from labs.lab2.domain.state import CalculatorState
from std.read import read_choose_from_list, read_until_pred


def config_action(opts: dict[str, Any], _: CalculatorState) -> None:
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

    parsed_val = parse(val)

    opts[chosen_opt] = parsed_val
    write_opts(opts)

    print(f"Set option {chosen_opt} to {parsed_val}.")
