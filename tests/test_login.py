from pages.login_page import PracticeLoginPage

def test_practice_login(page):
    login_page = PracticeLoginPage(page)

    # Step 1: Open login page
    login_page.open()

    # Step 2: Perform login
    login_page.login("student", "Password123")

    # Step 3: Verify success
    login_page.verify_login_success()
