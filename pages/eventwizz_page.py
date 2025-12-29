from playwright.sync_api import sync_playwright, Page


# ========== PAGE OBJECT MODEL ==========
class EventWizzPOM:
    def __init__(self, page: Page):
        self.page = page

    # Login page actions
    def open_login_page(self):
        self.page.goto("http://eventwizz.com:3000/auth/login")

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email address").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    # Dashboard actions
    def continue_to_dashboard(self):
    # Wait until redirected to select-location page
        self.page.wait_for_url("**/welcome/select-location", timeout=60000)

    # Now click button
        self.page.get_by_role("button", name="Continue to Dashboard").click()


    def open_create_event(self):
        self.page.get_by_role("link", name="Events").click()
        self.page.get_by_role("button", name="Create Event").click()


# ========== TEST ==========
def test_create_event_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        app = EventWizzPOM(page)

        app.open_login_page()
        app.login("adam@yopmail.com", "Test@1234")
        app.continue_to_dashboard()
        app.open_create_event()

        context.close()
        browser.close()
