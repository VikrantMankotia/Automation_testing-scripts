from playwright.sync_api import sync_playwright
from pages.filters_page import SauceDemoPage



def test_saucedemo_end_to_end():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")

        app = SauceDemoPage(page)

        app.login("standard_user", "secret_sauce")

        app.sort_products("za")
        app.add_product("add-to-cart-test.allthethings()-t-shirt-(red)")
        app.open_cart()

        app.continue_shopping_action()
        app.add_product("add-to-cart-sauce-labs-fleece-jacket")
        app.open_cart()

        app.checkout()
        app.fill_checkout_details("Vikrant", "Mankotia", "176214")
        app.finish_order()

        context.close()
        browser.close()
