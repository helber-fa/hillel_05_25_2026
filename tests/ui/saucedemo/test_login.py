import pytest
from playwright.sync_api import expect

from core.pages.login_page import LoginPage


@pytest.mark.ui
def test_login_positive(login_page):
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

        login_page.open()
        inventory_page = login_page.login_valid_user("standard_user", "secret_sauce")
        inventory_page.is_displayed()


