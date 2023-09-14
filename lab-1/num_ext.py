def try_parse_float(str_val: str) -> float | None:
    try:
        return float(str_val)
    except ValueError:
        return None
