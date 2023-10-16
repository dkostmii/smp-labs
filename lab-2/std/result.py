from typing import Any, Callable


class Ok:
    def __init__(self, val):
        self.val = val


class Err:
    def __init__(self, val):
        self.val = val

    def __repr__(self) -> str:
        msg = self.val if isinstance(self.val, str) else "Unknown error"

        return f"Error: {msg}"


class Result:
    ok_val: Ok | None
    err_val: Err | None

    def __init__(self, val):
        self.is_ok = False
        match val:
            case Ok():
                self.is_ok = True
                self.ok_val = val
                self.err_val = None
            case Err():
                self.ok_val = None
                self.err_val = val
            case _:
                raise Exception("Expected Ok or Err")

    def map(
        self, ok_accessor: Callable[[Any], None], err_accessor: Callable[[Any], None]
    ) -> None:
        if self.is_ok:
            ok_accessor(self.ok_val)
        else:
            err_accessor(self.err_val)
