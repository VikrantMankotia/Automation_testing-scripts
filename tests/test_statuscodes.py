from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

def test_navigate_to_status_codes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        home = HomePage(page)
        home.open()
        home.click_status_codes()

        # Assertions
        assert "status_codes" in page.url
        assert page.locator("h3").text_content() == "Status Codes"

        context.close()
        browser.close()
