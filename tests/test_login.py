import pytest
from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    # Step 1: Open login page
    login_page.open()

    # Step 2: Login
    login_page.login(
        username="student",
        password="Password123"
    )

    # Step 3: Assertion
    login_page.assert_login_success()
