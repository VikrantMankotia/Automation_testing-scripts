from playwright.sync_api import Page
class SauceDemoPage:
    def __init__(self, page):
        self.page = page

        # Login
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.login_btn = '[data-test="login-button"]'

        # Products
        self.sort_dropdown = '[data-test="product-sort-container"]'
        self.cart_icon = '[data-test="shopping-cart-link"]'

        # Cart
        self.checkout_btn = '[data-test="checkout"]'
        self.continue_shopping = '[data-test="continue-shopping"]'

        # Checkout
        self.first_name = '[data-test="firstName"]'
        self.last_name = '[data-test="lastName"]'
        self.postal_code = '[data-test="postalCode"]'
        self.continue_btn = '[data-test="continue"]'
        self.finish_btn = '[data-test="finish"]'
        self.back_home = '[data-test="back-to-products"]'

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def sort_products(self, value):
        self.page.select_option(self.sort_dropdown, value)

    def add_product(self, product_test_id):
        self.page.click(f'[data-test="{product_test_id}"]')

    def open_cart(self):
        self.page.click(self.cart_icon)

    def continue_shopping_action(self):
        self.page.click(self.continue_shopping)

    def checkout(self):
        self.page.click(self.checkout_btn)

    def fill_checkout_details(self, fname, lname, zip_code):
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.postal_code, zip_code)
        self.page.click(self.continue_btn)

    def finish_order(self):
        self.page.click(self.finish_btn)
        self.page.click(self.back_home)
