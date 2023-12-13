from .config import Config
from .service import UserService


class AppState:
    history: list[str] = []
    successful_result: bool = False
    response: dict | None = None
    user_profile_info: str | None = None
    user_service: UserService


def init_state(state: AppState, config: Config) -> AppState:
    state.user_service = UserService(config)
    return state
