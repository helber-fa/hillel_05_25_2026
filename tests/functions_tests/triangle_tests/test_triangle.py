# - core
# - data
# - test
#     - api
#         - some_api_connector
#             positive_test_cases
#             negative_test_cases
#                 some_test_function
#             specific_endpoint_tests
#     -db
#     -ui
#     -unit
import pytest
from python_practice.lesson22 import test_functions

@pytest.mark.triangle
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_triangle_1_1_1():
    area = test_functions.triangle_area(1,1,1)
    print("test1")
    assert round(area, 3) == 0.433
import os

@pytest.mark.triangle
@pytest.mark.regression
@pytest.mark.skipif(os.getenv("CURRENT_ENV", "Dev") == "Dev", reason="Flaky test, fix in progress")
def test_triangle_1_2_3():
    area = test_functions.triangle_area(1,2,3)
    print("test2")
    assert round(area, 3) == 0.433

@pytest.mark.triangle
@pytest.mark.negative
@pytest.mark.xfail(reason = "Known issue jira_id = 5579")
def test_triangle_value_error():
    with pytest.raises(TypeError):
        print("test3")
        test_functions.triangle_area(1,2,"3")

# def test_triangle_1_2_3():
#     area = test_functions.triangle_area(1,3,1)
#     assert round(area, 3) == 0.42