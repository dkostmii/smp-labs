import json
from typing import Any


def read_config(config_file_path: str = ".asciirc.json") -> dict[str, Any]:
    with open(file=config_file_path, mode="r", encoding="utf-8") as f:
        config = json.load(f)
        return config
