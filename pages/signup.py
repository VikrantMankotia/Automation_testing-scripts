from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

        # -------- Locators --------
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.locator("form").filter(
            has_text="Signup"
        ).get_by_placeholder("Email Address")
        self.signup_button = page.get_by_role("button", name="Signup")

        self.password_input = page.get_by_role("textbox", name="Password *")
        self.days_dropdown = page.locator("#days")
        self.months_dropdown = page.locator("#months")
        self.years_dropdown = page.locator("#years")

        self.first_name = page.get_by_role("textbox", name="First name *")
        self.last_name = page.get_by_role("textbox", name="Last name *")
        self.company = page.get_by_role("textbox", name="Company", exact=True)
        self.address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.state = page.get_by_role("textbox", name="State *")
        self.city = page.get_by_role("textbox", name="City * Zipcode *")
        self.zipcode = page.locator("#zipcode")
        self.mobile = page.get_by_role("textbox", name="Mobile Number *")

        self.create_account_btn = page.get_by_role("button", name="Create Account")
        self.continue_link = page.get_by_role("link", name="Continue")

    # -------- Actions --------
    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def signup_basic(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def fill_account_details(self):
        self.password_input.fill("Test@1234")
        self.days_dropdown.select_option("10")
        self.months_dropdown.select_option("7")
        self.years_dropdown.select_option("1912")

    def fill_address_details(self):
        self.first_name.fill("Vikrant")
        self.last_name.fill("Mankotia")
        self.company.fill("Socreative")
        self.address.fill("V.P.O Shamirpur, Kangra (H.P)")
        self.state.fill("Himachal Pradesh")
        self.city.fill("Kangra")
        self.zipcode.fill("176214")
        self.mobile.fill("7876856763")

    def submit_account(self):
        self.create_account_btn.click()
        self.continue_link.click()
