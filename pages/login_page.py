from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.success_text = page.locator("text=Logged In Successfully")

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def assert_login_success(self):
        expect(self.page).to_have_url(
            "https://practicetestautomation.com/logged-in-successfully/"
        )
        expect(self.success_text).to_be_visible()
