from actions.calc_action import calc_action
from actions.config_action import config_action
from actions.exit_action import exit_action
from actions.history_action import history_action
from actions.memory import clear_memory_action, save_to_memory_action
from domain.action import Action
from domain.calculator import Calculator, Runner

actions = [
    Action(name="Change config", action_fn=config_action),
    Action(name="Display history", action_fn=history_action),
    Action(name="Clear memory", action_fn=clear_memory_action),
    Action(name="Save to memory", action_fn=save_to_memory_action),
    Action(name="Do calculation", action_fn=calc_action),
    Action(name="Exit", action_fn=exit_action),
]


def main():
    calculator = Calculator(actions=actions)
    runner = Runner(calculator=calculator)
    runner.run()


if __name__ == "__main__":
    main()
