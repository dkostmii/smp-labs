import json
from os import get_terminal_size

import regex

from labs.lab7.domain.config import Config
from labs.lab7.domain.state import AppState
from labs.lab7.domain.table import convert_to_table
from std.read import read_choose_from_list, read_until_pred


def display_action(_: Config, state: AppState):
    username = read_until_pred(
        pred=lambda username: isinstance(username, str)
        and bool(regex.match(r"^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$", username)),
        title="Enter username: ",
        invalid_msg="Username is invalid.",
    )

    term_size = get_terminal_size()
    (term_width, term_height) = (term_size.columns, term_size.lines)
    term_char_count = term_width * term_height

    try:
        state.response = state.user_service.get_personal_profile(username)

        display_as = read_choose_from_list(
            ["table", "JSON"], title="How do you want display result?"
        )

        if display_as == "table":
            state.user_profile_info = convert_to_table(json.dumps(state.response))
            print(state.user_profile_info)
            state.history.append(
                f"Data of a personal profile where username is {username}:\n{state.user_profile_info}"
            )
            state.successful_result = True
        elif display_as == "JSON":
            state.user_profile_info = json.dumps(state.response, indent=4)
            print(state.user_profile_info[:term_char_count])
            state.history.append(
                f"Data of a personal profile where username is {username}:\n{state.user_profile_info}"
            )
            state.successful_result = True
        else:
            raise Exception(f"Unexpected error. Invalid option: {display_as}")
    except ValueError as e:
        print(e)
        state.successful_result = False
        state.response = None
        state.user_profile_info = None
        state.history.append(str(e))
