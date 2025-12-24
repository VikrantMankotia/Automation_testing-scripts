from playwright.sync_api import Page

class RioLoginPage:
    def __init__(self, page: Page):
        self.page = page

        # ✅ Correct locators (based on real HTML)
        self.username_input = "#email"                    # id="email"
        self.password_input = "input[name='password']"   # adjust if needed
        self.login_button = "button[type='submit']"

    def open_login_page(self):
        self.page.goto("http://eventwizz.com:3000/auth/login")
        self.page.wait_for_load_state("networkidle")

    def enter_username(self, username):
        self.page.wait_for_selector(self.username_input)
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.wait_for_selector(self.password_input)
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.wait_for_selector(self.login_button)
        self.page.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
