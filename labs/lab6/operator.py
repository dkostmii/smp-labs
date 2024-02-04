import unittest
from typing import cast

from domain.operation import OperationError, apply_op, operators
from std.result import Result


class AdditionTests(unittest.TestCase):
    def _add_test(self, a: float, b: float):
        expected = a + b

        actual = apply_op(operators["+"], (a, b))
        self.assertEqual(expected, actual)

    def add_positive_test(self):
        self._add_test(a=3, b=4)

    def add_negative_test(self):
        self._add_test(a=-5, b=-1)


class SubtractionTests(unittest.TestCase):
    def _sub_test(self, a: float, b: float):
        expected = a - b

        actual = apply_op(operators["-"], (a, b))
        self.assertEqual(expected, actual)

    def sub_positive_test(self):
        self._sub_test(a=2, b=1)

    def sub_negative_test(self):
        self._sub_test(a=-3, b=11)


class MultiplicationTests(unittest.TestCase):
    def _mul_test(self, a: float, b: float):
        expected = a * b

        actual = apply_op(operators["*"], (a, b))
        self.assertEqual(expected, actual)

    def mul_positive_test(self):
        self._mul_test(a=3, b=8)

    def mul_zero_test(self):
        self._mul_test(a=0, b=6)

    def mul_negative_test(self):
        self._mul_test(a=-2, b=-9)


class DivisionTests(unittest.TestCase):
    def _div_test(self, a: float, b: float):
        actual = apply_op(operators["/"], (a, b))
        self.assertIsInstance(actual, Result)
        actual = cast(Result[float, OperationError], actual)

        if b == 0:
            self.assertFalse(actual.is_ok)
            self.assertIsNone(actual.ok)
            self.assertIsInstance(actual.err, OperationError)
            op_err = cast(OperationError, actual.err)
            self.assertEqual(op_err.message, "Cannot divide by zero.")
            self.assertEqual(str(op_err), "Operation error: Cannot divide by zero.")

            return

        expected = a / b
        self.assertTrue(actual.is_ok)
        self.assertIsNone(actual.err)
        self.assertIsInstance(actual.ok, float)
        op_ok = cast(float, actual.ok)
        self.assertEqual(op_ok, expected)

    def div_positive_test(self):
        self._div_test(a=2, b=8)

    def div_zero_test(self):
        self._div_test(a=0, b=4)

    def div_zero_div_err_test(self):
        self._div_test(a=8, b=0)

    def div_negative_test(self):
        self._div_test(a=-3, b=2)
