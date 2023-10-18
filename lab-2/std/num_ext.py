def try_parse_float(str_val: str) -> float | None:
    try:
        return float(str_val)
    except ValueError:
        return None


def try_parse_int(str_val: str) -> int | None:
    try:
        return int(str_val)
    except ValueError:
        return None
