from calc import CalculatorState
from typing import Any

from config.opts import write_opts, validators
from config.defaults import defaults

from std.read import read_single_num, read_choose_from_list


def change_config_proc(opts: dict[str, Any], state: CalculatorState) -> None:
    available_opts = list(defaults.keys())
    chosen_opt = read_choose_from_list(available_opts, "Choose config option to change: ")

    validator = validators[chosen_opt]

    val = read_single_num(f"Enter a value for {chosen_opt}: ")

    while not validator(val):
        print(f"Enter a valid value for {chosen_opt}: ")
        val = read_single_num()

    opts[chosen_opt] = int(val)
    write_opts(opts)

