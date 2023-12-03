import json
from lab5.domain.types import Point3F

def get_object_dict() -> dict[str, list[Point3F]]:
    with open("lab5/data/objects.json", mode="r", encoding="utf-8") as f:
        object_dict: dict[str, list[Point3F]] = json.load(f)

    return object_dict
