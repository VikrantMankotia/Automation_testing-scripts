class SignupPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.login_link = page.get_by_role("link", name="Log in")
        self.signup_link = page.get_by_role("link", name="Sign Up")
        self.email_input = page.get_by_role(
            "textbox", name="Business Email address"
        )
        self.verify_button = page.get_by_role(
            "button", name="Verify email ⟩"
        )

    def open_signup_page(self):
        self.page.goto("https://eventwizz.vercel.app/", timeout=60000)
        self.login_link.click()
        self.signup_link.click()

    def signup_with_email(self, email):
        self.email_input.fill(email)
        self.verify_button.click()
