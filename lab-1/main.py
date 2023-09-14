from ops import read_op, apply_op, display_op_res
from read import read_yes_no

def main():
    repeat_requested = True

    print("Welcome to awesome calculator ;)")
    while repeat_requested:
        repeat_requested = False
        op, values = read_op()
        op_res = apply_op(op, values)
        display_op_res(op_res)

        repeat_requested = read_yes_no(
            title="Do you want continue?",
            default=False)


if __name__ == "__main__":
    main()

