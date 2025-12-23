from playwright.sync_api import Page


class SauceDemoPage:
    def __init__(self, page: Page):
        self.page = page

        # Login locators
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.login_btn = '[data-test="login-button"]'

        # Inventory / Cart locators
        self.add_backpack = '[data-test="add-to-cart-sauce-labs-backpack"]'
        self.cart_link = '[data-test="shopping-cart-link"]'
        self.remove_backpack = '[data-test="remove-sauce-labs-backpack"]'

    def open_site(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user: str, pwd: str):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def add_item_to_cart(self):
        self.page.click(self.add_backpack)

    def open_cart(self):
        self.page.click(self.cart_link)

    def remove_item_from_cart(self):
        self.page.click(self.remove_backpack)
