from lab2.actions import actions
from lab2.domain.calculator import Calculator
from runner import Runner


def main():
    calculator = Calculator(actions=actions)
    runner = Runner(app=calculator)
    runner.run()


if __name__ == "__main__":
    main()
