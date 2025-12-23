from playwright.sync_api import sync_playwright
from pages.saucedemo_page import SauceDemoPage


def test_add_and_remove_item():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        sauce_page = SauceDemoPage(page)

        sauce_page.open_site()
        sauce_page.login("standard_user", "secret_sauce")
        sauce_page.add_item_to_cart()
        sauce_page.open_cart()
        sauce_page.remove_item_from_cart()

        context.close()
        browser.close()
