from playwright.sync_api import Page


class ChatPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.chat_link = page.get_by_role("link", name="CHAT WITH CLIVE", exact=True)
        self.chat_input = page.get_by_role("textbox", name="Ask your financial question...")
        self.send_button = page.get_by_role("button", name="Send", exact=True)

    def open_homepage(self):
        self.page.goto("https://www.helloclive.com/")

    def open_chat(self):
        self.chat_link.click()

    def send_message(self, message: str):
        self.chat_input.click()
        self.chat_input.fill(message)
        self.chat_input.press("Enter")
        self.send_button.click()
