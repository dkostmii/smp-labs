import unittest

from .profile import TestGetPersonalProfile


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGetPersonalProfile("test_get_personal_profile_success"))
    suite.addTest(TestGetPersonalProfile("test_get_personal_profile_error_response"))

    return suite


def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
