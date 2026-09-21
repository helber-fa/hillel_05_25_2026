import time

import allure
import pytest
from playwright.sync_api import expect

from core.data.login_data import INVALID_LOGIN_DATA
from core.data.login_data import STANDARD_LOGIN
from core.pages.login_page import LoginPage

# @pytest.mark.ui
# def test_login_positive(login_page):
        # browser = playwright.chromium.launch(
        #     headless=False,
        #     args=["--start-maximized"])
        # context = browser.new_context(
        #     no_viewport=True
        # )
        # page = context.new_page()
        # page.goto("https://www.saucedemo.com")
        # page.wait_for_timeout(3000)
        # username_locator = page.locator("//input[@placeholder='Username']")
        # username_locator.fill("standard_user")
        #
        # pass_locator = page.locator("#password")
        # pass_locator.fill("secret_sauce")
        #
        # page.get_by_role("button", name="Login").click()

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.ui
def test_login_positive(login_page):
        login_page.open()
        inventory_page = login_page.login_valid_user(STANDARD_LOGIN.username, STANDARD_LOGIN.password)
        inventory_page.is_displayed()
        inventory_page.img_loaded()

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.ui
def test_login_click_enter(login_page):
        login_page.open()
        inventory_page = login_page.login_via_enter(STANDARD_LOGIN.username, STANDARD_LOGIN.password)
        inventory_page.is_displayed()
        inventory_page.img_loaded()

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.parametrize(
        "test_data",
        INVALID_LOGIN_DATA,
        ids=[
                "wrong_password",
                "empty_username",
                "locked_out_user"
        ]
)
def test_login_wrong_password(login_page, test_data):
        login_page.open()
        login_page.do_invalid_login(test_data.username, test_data.password)
        assert login_page.get_error_message() == test_data.expected_error
        # (expect(login_page.get_error_element()).
        #  to_have_text("Epic sadface: Username and password do not match any user in this service"))
        # (expect(login_page.get_error_element())
        #  .to_contain_text("Epic sadface"))






