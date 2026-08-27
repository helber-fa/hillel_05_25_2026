from playwright.sync_api import Page, expect

from core.pages.base_page import BasePage


class InventoryPage(BasePage):
    APP_LOGO = ".app_logo"

    def __init__(self, page:Page):
        super().__init__(page)

    def is_displayed(self):
        expect(self.page.locator(self.APP_LOGO)).to_be_visible()