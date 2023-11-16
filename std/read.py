import sys
from typing import Any, Callable

from std.num_ext import try_parse_int, try_parse_float

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


def read_single_int(title: str = "") -> int:
    num_str = input_wrapper(title)
    num = try_parse_int(num_str)

    while num is None:
        print("Enter a valid number.")
        num_str = input_wrapper(title)
        num = try_parse_int(num_str)

    return num


def read_single_float(title: str = "") -> int:
    num_str = input_wrapper(title)
    num = try_parse_float(num_str)

    while num is None:
        print("Enter a valid number.")
        num_str = input_wrapper(title)
        num = try_parse_float(num_str)

    return num


def default_formatter(value: Any) -> str:
    return str(value)


def read_choose_from_list(
    options: list[Any],
    title: str = "",
    formatter: Callable[[Any], str] = default_formatter,
) -> Any:
    print(title)

    for n, item in enumerate(options):
        print(f"{n + 1}. {formatter(item)}")

    option_n = read_until_pred_custom(
        read_single_int,
        lambda v: 0 < int(v) <= len(options),
        "Your choice: ",
        "Invalid option number.",
    )

    return options[option_n - 1]


def is_writable(filename: str) -> bool:
    with open(filename, "a") as f:
        return f.writable()


def is_readable(filename: str) -> bool:
    with open(filename, "r") as f:
        return f.readable()


def read_filename(
    title: str = "", check_writable: bool = False, check_readable: bool = False
) -> str:
    invalid = True

    while invalid:
        filename_input = input_wrapper(title)
        invalid = (check_writable and not is_writable(filename_input)) or (
            check_readable and not is_readable(filename_input)
        )

        if not invalid:
            return filename_input
        else:
            permissions = []

            if check_writable:
                permissions.append("read")

            if check_readable:
                permissions.append("write")

            permissions_caption = " and ".join(permissions)
            print(
                f"You do not have permssions to {permissions_caption} {filename_input} file. Please try again."
            )

    raise Exception("This exception must be unreachable")
