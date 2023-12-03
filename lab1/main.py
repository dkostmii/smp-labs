from lab1.config.opts import read_opts
from lab1.domain.state import CalculatorState
from lab1.procedures import Procedure
from lab1.procedures.calc import do_calculation_proc
from lab1.procedures.config import change_config_proc
from lab1.procedures.exit_proc import exit_proc
from lab1.procedures.history_proc import display_history_proc
from lab1.procedures.memory import clear_memory_proc, save_to_memory_proc
from std.read import read_choose_from_list, read_yes_no

operations: dict[str, Procedure] = {
    "change_config": change_config_proc,
    "display_history": display_history_proc,
    "clear_memory": clear_memory_proc,
    "save_to_memory": save_to_memory_proc,
    "do_calculation": do_calculation_proc,
    "exit": exit_proc,
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

        repeat_requested = read_yes_no(title="Do you want to continue?", default=False)


if __name__ == "__main__":
    main()