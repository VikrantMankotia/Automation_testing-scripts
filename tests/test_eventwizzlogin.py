from pages.eventwizzlogin_page import RioLoginPage

def test_rio_valid_login(page):
    login_page = RioLoginPage(page)

    login_page.open_login_page()
    login_page.login("testuser", "testpassword")

    # Optional validation (example)
    # expect(page).to_have_url("https://example.com/dashboard")
