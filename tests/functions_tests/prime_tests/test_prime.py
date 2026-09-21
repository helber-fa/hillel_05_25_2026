# щоб запусти pytest, файл, клас та функція мають містити test в назві
import os.path

import allure
import pytest

from constants import BASE_PROJECT_PATH
from python_practice.lesson22 import test_functions


@pytest.mark.prime
class TestPrimePositive:

    @allure.epic("Unit")
    @pytest.mark.parametrize("input_value,expected_result", [
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (11, [2, 3, 5, 7, 11]),
        (5, [2, 3, 5])
    ])
    def test_prime(self, input_value, expected_result):

        with open(f"{os.path.join(BASE_PROJECT_PATH, 'results', str(input_value))}.txt", "w") as f:
            f.write("test results")

        primes_list = test_functions.find_primes(input_value)
        assert primes_list == expected_result



