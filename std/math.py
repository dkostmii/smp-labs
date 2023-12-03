def map(value: float, min_input: float, max_input: float, min_output: float, max_output: float) -> float:
    abs_value = (value - min_input) / (max_input - min_input)
    out_value = (abs_value * (max_output - min_output)) + min_output

    return out_value


def get_window(window_size: int, offset: float, items: list) -> list:
    if offset < 0:
        raise Exception("Too small offset")

    if offset > len(items) - window_size:
        raise Exception("Too large offset")

    return items[offset:(offset + window_size)]


def sign(num: float) -> float:
    if num == 0:
        return 0

    return num / abs(num)
