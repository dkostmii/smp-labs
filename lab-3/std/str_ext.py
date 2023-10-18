def pad_left(text: str, count: int = 0, pad_char: str = " ") -> str:
    if count < 1:
        return text

    return (pad_char * count) + text


TOP = "TOP"
BOTTOM = "BOTTOM"


def pad_vertical(text: str, count: int = 0, type: str = TOP, newline_char="\n") -> str:
    if type != TOP and type != BOTTOM:
        raise Exception(f"Invalid padding type: {type}")

    text_lines = text.split(newline_char)

    if count < 1:
        return text

    padding = [""] * count

    result = text_lines

    if type == TOP:
        result = padding + text_lines
    elif type == BOTTOM:
        result = text_lines + padding

    return newline_char.join(result)


def pad_top(text: str, count: int = 0, newline_char="\n") -> str:
    return pad_vertical(text=text, count=count, type=TOP, newline_char=newline_char)


def pad_bottom(text: str, count: int = 0, newline_char="\n") -> str:
    return pad_vertical(text=text, count=count, type=BOTTOM, newline_char=newline_char)
