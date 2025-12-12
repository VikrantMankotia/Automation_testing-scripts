from playwright.sync_api import Page, expect

class PracticeLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Submit")

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def verify_login_success(self):
        expect(self.page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
        expect(self.page.get_by_text("Congratulations")).to_be_visible()
