class HomePage:
    def __init__(self, page):
        self.page = page

    STATUS_CODES_LINK = "text=Status Codes"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/")

    def click_status_codes(self):
        self.page.click(self.STATUS_CODES_LINK)
