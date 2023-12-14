from typing import Any

# Obtain API key for https://rapidapi.com/neotank/api/instagram130/


class Config:
    api_key: str
    api_host: str
    api_endpoints: dict[str, str]
    filter_response: list[str] | None

    def __init__(self, config_data: dict[str, Any]):
        self.api_key = config_data["X_RapidApi_Key"]
        self.api_host = config_data["X_RapidApi_Host"]
        self.api_endpoints = config_data["endpoints"]
        self.filter_response = config_data["filter_response"]
