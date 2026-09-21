import time
import unittest

import allure

from core.api.gorest_controller.gorest_controller import GorestController

gorest_controller = GorestController()
class TestUserCreate(unittest.TestCase):
    @allure.epic("API")
    @allure.feature("Gorest feature")
    @allure.story("Create user")
    def test_create_user(self):
        user_data = { "name": "Tenali Ramakrishna", "email": f"tenali@{time.time()}example.com",
                      "gender": "male", "status": "active" }

        response = gorest_controller.create_user(user_data)
        print(response.text)
        self.assertEqual(201, response.status_code)