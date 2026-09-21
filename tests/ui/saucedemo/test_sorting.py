import time

import allure
import pytest

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test sorting")
@allure.title("Check sorting - price ascending")
@allure.description("This test checks sorting of elements based on price from low to high")
@allure.tag( "positive", "sorting")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jira/4553")
@pytest.mark.ui
def test_sorting_price_asc(login_page):
        login_page.open()
        inventory_page = login_page.login_valid_user("standard_user", "secret_sauce")

        inventory_page.sort_by("Price (low to high)")
        expect_sorted_prices = inventory_page.collect_price()

        assert expect_sorted_prices == sorted(expect_sorted_prices)
