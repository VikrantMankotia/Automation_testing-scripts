from playwright.sync_api import sync_playwright
from pages.chat_page import ChatPage


def test_chat_with_clive():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        chat_page = ChatPage(page)

        # Steps
        chat_page.open_homepage()
        chat_page.open_chat()

        chat_page.send_message("hey")
        chat_page.send_message("seen")
        chat_page.send_message("seen")

        context.close()
        browser.close()
