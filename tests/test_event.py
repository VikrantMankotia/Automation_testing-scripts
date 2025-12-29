from playwright.sync_api import sync_playwright
from pages.eventwizz_page import EventWizzPOM   # if POM is in same file, ignore this import


def test_vendor_can_open_create_event_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        app = EventWizzPOM(page)

        # Step 1: Open login page
        app.open_login_page()

        # Step 2: Login
        app.login("adam@yopmail.com", "Test@1234")

        # Step 3: Continue to dashboard
        app.continue_to_dashboard()

        # Step 4: Open Create Event page
        app.open_create_event()

        # (Optional assertion – add if element exists)
        # assert page.url.__contains__("event")

        context.close()
        browser.close()
