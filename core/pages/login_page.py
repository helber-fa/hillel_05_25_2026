from playwright.sync_api import Page

from core.pages.base_page import BasePage
from core.pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"

    def __init__(self, page:Page):
        super().__init__(page)

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login_valid_user(self, username, password):
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.get_by_role("button", name="Login").click()
        return InventoryPage(self.page)
