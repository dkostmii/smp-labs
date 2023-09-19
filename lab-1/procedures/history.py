from calc import CalculatorState

from typing import Any

def display_history_proc(config: dict[str, Any], state: CalculatorState) -> None:

    history_count = int(config["history_count"])
    print(f"Last {history_count} entries are:")

    for entry in state.history:
        result_str = ""
        match entry.result:
            case float():
                result_str = entry.result
            case _:
                result_str = "ERR"

        entry_str = f"{entry.operation_str} = {result_str}"
        print(entry_str)

