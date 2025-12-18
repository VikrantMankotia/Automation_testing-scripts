from playwright.sync_api import sync_playwright
from pages.practice_form import PracticeFormPage


def test_practice_form_submission():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        form_page = PracticeFormPage(page)

        form_page.open_practice_form()
        form_page.fill_basic_details()
        form_page.select_date_of_birth()
        form_page.fill_subjects_and_hobbies()
        form_page.fill_address()
        form_page.select_state_and_city()
        form_page.submit_form()
        form_page.verify_submission()

        context.close()
        browser.close()
