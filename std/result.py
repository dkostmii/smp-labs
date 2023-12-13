from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")


class Ok:
    def __init__(self, val):
        self.val = val


class TypedOk(Generic[T]):
    val: T

    def __init__(self, val: T):
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
    is_ok: bool

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


class TypedResult(Generic[T]):
    ok_val: TypedOk[T] | None
    err_val: Err | None
    is_ok: bool

    def __init__(self, val: TypedOk[T] | Err):
        self.is_ok = False
        match val:
            case TypedOk():
                self.is_ok = True
                self.ok_val = val
                self.err_val = None
            case Err():
                self.ok_val = None
                self.err_val = val
            case _:
                raise Exception("Expected TypedOk or Err")

    def map(
        self,
        ok_accessor: Callable[[TypedOk], None],
        err_accessor: Callable[[Err], None],
    ) -> None:
        if self.is_ok and isinstance(self.ok_val, TypedOk):
            ok_accessor(self.ok_val)
        elif isinstance(self.err_val, Err):
            err_accessor(self.err_val)
        else:
            raise Exception(
                "Unexpected error. TypedResult must contain either ok_val or err_val."
            )
