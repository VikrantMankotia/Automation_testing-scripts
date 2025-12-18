from playwright.sync_api import Page, expect


class PracticeFormPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.email = page.get_by_role("textbox", name="name@example.com")
        self.mobile = page.get_by_role("textbox", name="Mobile Number")
        self.address = page.get_by_role("textbox", name="Current Address")
        self.submit_btn = page.get_by_role("button", name="Submit")

    # ---------- Actions ----------

    def open_practice_form(self):
     self.page.goto("https://demoqa.com/")
     self.page.get_by_role("heading", name="Forms").click()
     self.page.get_by_text("Practice Form").click()

    # REMOVE ads & fixed banners that block clicks
     self.page.evaluate("""
        const ads = document.querySelectorAll('#fixedban, iframe');
        ads.forEach(ad => ad.remove());
    """)

    def fill_basic_details(self):
        self.first_name.fill("Vikrant")
        self.last_name.fill("Mankotia")
        self.email.fill("vikrantmankotia2918@gmail.com")
        self.page.get_by_text("Male", exact=True).click()
        self.mobile.fill("7876856763")

    def select_date_of_birth(self):
        self.page.locator("#dateOfBirthInput").click()
        self.page.get_by_role("combobox").nth(1).select_option("1969")
        self.page.get_by_role(
            "option", name="Choose Tuesday, December 16th,"
        ).click()

        # IMPORTANT: Close calendar overlay
        self.page.keyboard.press("Escape")
        self.page.locator(".react-datepicker").wait_for(state="hidden")

    def fill_subjects_and_hobbies(self):
        # Subject
        subject_input = self.page.locator("#subjectsInput")
        subject_input.fill("Testing")
        self.page.keyboard.press("Enter")

        # Hobbies
        self.page.get_by_text("Sports", exact=True).click()
        self.page.get_by_text("Reading", exact=True).click()
        self.page.get_by_text("Music", exact=True).click()

    def fill_address(self):
        self.address.fill("Kangra, Himachal Pradesh")

    def select_state_and_city(self):
        self.page.locator(".css-19bqh2r").first.click()
        self.page.get_by_text("NCR", exact=True).click()

        self.page.get_by_text("Select City").click()
        self.page.get_by_text("Gurgaon", exact=True).click()

    def submit_form(self):
        self.submit_btn.click()

    def verify_submission(self):
        modal = self.page.get_by_role(
            "dialog", name="Thanks for submitting the form"
        )
        expect(modal).to_be_visible()
