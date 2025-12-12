from playwright.sync_api import Page, expect

class AddToCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.product_link = page.locator("[data-test='item-4-title-link']")
        self.add_to_cart_button = page.locator("[data-test='add-to-cart']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self):
        self.username_input.fill("standard_user")
        self.password_input.fill("secret_sauce")
        self.login_button.click()

    def add_product_to_cart(self):
        self.product_link.click()
        self.add_to_cart_button.click()
        self.cart_link.click()

    def verify_cart(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
