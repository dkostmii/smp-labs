from std.read import read_yes_no, read_choose_from_list

from procedures.config import change_config_proc
from procedures.history import display_history_proc
from procedures.memory import clear_memory_proc, save_to_memory_proc
from procedures.ops import do_calculation_proc

from config.opts import read_opts
from calc import CalculatorState


operations = {
        "change_config": change_config_proc,
        "display_history": display_history_proc,
        "clear_memory": clear_memory_proc,
        "save_to_memory": save_to_memory_proc,
        "do_calculation": do_calculation_proc,
}


def main():
    repeat_requested = True

    print("Welcome to awesome calculator ;)")

    available_procedures = list(operations.keys())

    # Pass the state to every procedure
    state = CalculatorState()

    while repeat_requested:
        operation = read_choose_from_list(available_procedures, "Choose operation: ")

        proc = operations[operation]
        proc(read_opts(), state)

        repeat_requested = read_yes_no(
            title="Do you want to continue?",
            default=False)


if __name__ == "__main__":
    main()

