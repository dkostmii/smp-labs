import unittest

from .operator import (AdditionTests, DivisionTests, MultiplicationTests,
                       SubtractionTests)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AdditionTests("add_positive_test"))
    suite.addTest(AdditionTests("add_negative_test"))
    suite.addTest(SubtractionTests("sub_positive_test"))
    suite.addTest(SubtractionTests("sub_negative_test"))
    suite.addTest(MultiplicationTests("mul_positive_test"))
    suite.addTest(MultiplicationTests("mul_negative_test"))
    suite.addTest(MultiplicationTests("mul_zero_test"))
    suite.addTest(DivisionTests("div_positive_test"))
    suite.addTest(DivisionTests("div_zero_test"))
    suite.addTest(DivisionTests("div_zero_div_err_test"))
    suite.addTest(DivisionTests("div_negative_test"))

    return suite


def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())


if __name__ == "__main__":
    main()
