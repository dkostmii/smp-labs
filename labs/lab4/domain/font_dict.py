import json

from domain.types import Point


def get_font_dict() -> dict[str, list[Point]]:
    with open("labs/lab4/data/fonts.json", mode="r", encoding="utf-8") as f:
        font_dict: dict[str, list[Point]] = json.load(f)

    return font_dict
