import sys
from typing import Any, Callable

from std.num_ext import try_parse_float

YES = "yes"
NO = "no"


def input_wrapper(prompt: str = "") -> str:
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print()
        sys.exit(0)


def read_until_pred_custom(
    custom_src: Callable[[str], Any],
    pred: Callable[[Any], bool],
    title: str = "",
    invalid_msg: str | None = None,
) -> Any:
    val = custom_src(title)

    while not pred(val):
        if invalid_msg is not None:
            print(invalid_msg)

        val = custom_src(title)

    return val


def read_until_pred(
    pred: Callable[[str], bool], title: str = "", invalid_msg: str | None = None
) -> str:
    val = read_until_pred_custom(input_wrapper, pred, title, invalid_msg)
    return val


def read_yes_no(title: str = "", default: bool = False) -> bool:
    yes_str = YES
    no_str = NO

    if default:
        yes_str = yes_str.upper()
    else:
        no_str = no_str.upper()

    if len(title) > 0:
        yes_str = yes_str[0]
        no_str = no_str[0]
        val = input_wrapper(f"{title} [{yes_str}/{no_str}]: ")
    else:
        val = input_wrapper(f"{yes_str} or {no_str}\\?: ")

    val = val.lower()
    yes_str = yes_str.lower()
    no_str = no_str.lower()

    return val != no_str if default else val == yes_str


def read_single_num(title: str = "") -> float:
    num_str = input_wrapper(title)
    num = try_parse_float(num_str)

    while num is None:
        print("Enter a valid number.")
        num_str = input_wrapper(title)
        num = try_parse_float(num_str)

    return num


def read_choose_from_list(options: list[str], title: str = "") -> str:
    print(title)

    for n, item in enumerate(options):
        print(f"{n + 1}. {item}")

    option_n = read_until_pred_custom(
        read_single_num,
        lambda v: 0 < int(v) and int(v) <= len(options),
        "Your choice: ",
        "Invalid option number.",
    )
    option_n = int(option_n)

    return options[option_n - 1]
