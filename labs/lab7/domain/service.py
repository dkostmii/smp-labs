from typing import Any

import regex
import requests

from .config import Config


def get_keys(keys: list[str], data: dict[str, Any]):
    result: dict[str, Any] = {}

    for key in keys:
        result[key] = data[key]

    return result


class UserService:
    def __init__(self, config: Config):
        self.config = config

    def get_personal_profile(self, username: str):
        config = self.config

        if (
            username is None
            or not isinstance(username, str)
            or not regex.match(r"^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$", username)
        ):
            raise ValueError(
                "Username is supposed to be a string, or it has an incorrect value according to the rules!"
            )

        querystring = {"username": username}

        headers = {"X-RapidAPI-Key": config.api_key, "X-RapidAPI-Host": config.api_host}

        response = requests.get(
            config.api_endpoints["get_personal_profile"],
            headers=headers,
            params=querystring,
        )
        if response.status_code != 200:
            message: str = response.json().get("message", "Unknown error occurred!")
            raise ValueError(f"Error occurred! {message}")
        else:
            json = response.json()

            if (
                isinstance(config.filter_response, list)
                and len(config.filter_response) > 0
            ):
                json = get_keys(config.filter_response, json)

            return json
