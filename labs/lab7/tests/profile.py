import unittest

from helpers.api_config import read_config
from labs.lab7.domain.config import Config
from labs.lab7.domain.service import UserService


class TestGetPersonalProfile(unittest.TestCase):
    config: Config

    @classmethod
    def setUpClass(cls):
        cls.config = Config(config_data=read_config("config/lab7.json"))

    def test_get_personal_profile_success(self):
        user_service = UserService(config=self.config)

        username = "instagram"
        expected_id = "25025320"
        result = user_service.get_personal_profile(username)
        self.assertEqual(result["id"], expected_id)

    def test_get_personal_profile_error_response(self):
        user_service = UserService(config=self.config)

        username = "42dawjdjad\\daw+-@312"

        with self.assertRaises(ValueError):
            user_service.get_personal_profile(username)
