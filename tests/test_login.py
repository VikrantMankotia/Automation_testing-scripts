from playwright.sync_api import expect

def test_practice_login(page):

    # Step 1: Open the login page
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Step 2: Enter username
    page.get_by_role("textbox", name="Username").fill("student")

    # Step 3: Enter password
    page.get_by_role("textbox", name="Password").fill("Password123")

    # Step 4: Click submit
    page.get_by_role("button", name="Submit").click()

    # Step 5: Assert success
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.get_by_text("Congratulations")).to_be_visible()
