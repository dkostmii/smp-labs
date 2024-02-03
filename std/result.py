from typing import Callable, Generic, TypeVar, cast

TOk = TypeVar("TOk")
TErr = TypeVar("TErr")


class Ok(Generic[TOk]):
    def __init__(self, val: TOk):
        self.val = val


class Err(Generic[TErr]):
    def __init__(self, val: TErr):
        self.val = val

    def __repr__(self) -> str:
        msg = repr(self.val)

        return f"Error: {msg}"


class Result(Generic[TOk, TErr]):
    _val: Ok[TOk] | Err[TErr]

    @property
    def is_ok(self):
        return isinstance(self._val, Ok)

    @property
    def is_err(self):
        return isinstance(self._val, Err)

    def __init__(self, val: Ok[TOk] | Err[TErr]):
        self._val = val

    @property
    def ok(self) -> TOk | None:
        if not self.is_ok:
            return None

        return cast(Ok[TOk], self._val).val

    @property
    def err(self) -> TErr | None:
        if not self.is_err:
            return None

        return cast(Err[TErr], self._val).val

    def map(
        self, ok_accessor: Callable[[TOk], None], err_accessor: Callable[[TErr], None]
    ):
        if self.is_ok:
            ok_accessor(cast(TOk, self.ok))
        elif self.is_err:
            err_accessor(cast(TErr, self.err))
