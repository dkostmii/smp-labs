from labs.lab7.domain.config import Config
from labs.lab7.domain.state import AppState
from std import io
from std.read import read_choose_from_list, read_filename


def save_file_action(_: Config, state: AppState):
    if len(state.history) == 0:
        print("No request made")
        return

    if not (state.successful_result and state.user_profile_info and state.response):
        print("Request has failed. Cannot save data to a file")
        return

    save_as = read_choose_from_list(
        ["text", "JSON", "CSV"], title="How do you want to save the data?"
    )

    if save_as == "text":
        io.write_into_file(
            read_filename(
                "Enter text file name: ", check_writable=True, check_readable=False
            ),
            state.user_profile_info,
        )
    elif save_as == "JSON":
        io.write_into_json(
            read_filename(
                "Enter JSON file name: ", check_writable=True, check_readable=False
            ),
            state.response,
        )
    elif save_as == "CSV":
        io.write_into_csv(
            read_filename(
                "Enter CSV file name: ", check_writable=True, check_readable=False
            ),
            state.response,
        )
    else:
        raise Exception(f"Unexpected error. Invalid option {save_as}")
