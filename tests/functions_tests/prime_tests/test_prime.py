# щоб запусти pytest, файл, клас та функція мають містити test в назві
import pytest

from python_practice.lesson22 import test_functions


@pytest.mark.prime
class TestPrimePositive:

    @pytest.mark.parametrize("input_value,expected_result", [
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (11, [2, 3, 5, 7, 11]),
        (5, [2, 3, 5])
    ])
    def test_prime(self, input_value, expected_result):
        primes_list = test_functions.find_primes(input_value)
        assert primes_list == expected_result



