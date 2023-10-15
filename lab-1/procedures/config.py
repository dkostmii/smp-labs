from typing import Any

from config.defaults import defaults
from config.opts import validators, write_opts
from domain.state import CalculatorState
from std.read import read_choose_from_list, read_single_num


def change_config_proc(opts: dict[str, Any], state: CalculatorState) -> None:
    available_opts = list(defaults.keys())
    chosen_opt = read_choose_from_list(
        available_opts, "Choose config option to change: "
    )

    validator = validators[chosen_opt]

    val = read_single_num(f"Enter a value for {chosen_opt}: ")

    while not validator(val):
        print(f"Enter a valid value for {chosen_opt}: ")
        val = read_single_num()

    opts[chosen_opt] = int(val)
    write_opts(opts)
