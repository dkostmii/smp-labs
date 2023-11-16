from typing import Any


class TextConfig:
    max_length: int
    default: str

    def __init__(self, max_length: int = 0, default: str = "Hello, World!"):
        if max_length < 1:
            self.max_length = 0
        else:
            self.max_length = max_length

        if len(default) < 1:
            self.default = "Hello, World!"
        else:
            self.default = default

        self.default = self.default[:max_length]


class Config:
    fonts: list[str]
    text: TextConfig

    def __init__(self, config_data: dict[str, Any]):
        if not (
            isinstance(config_data["fonts"], list)
            and all(isinstance(item, str) for item in config_data["fonts"])
        ):
            raise Exception('Expected "fonts" key of config to be list of strings')

        if isinstance(config_data["text"], dict):
            self.text = TextConfig(
                max_length=config_data["text"]["maxLength"],
                default=config_data["text"]["default"],
            )
        else:
            self.text = TextConfig()

        self.fonts = config_data["fonts"]
