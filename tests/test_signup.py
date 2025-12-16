from pages.signup import SignupPage
from playwright.sync_api import expect
import re





def test_user_signup(page):
    signup = SignupPage(page)

    # Step 1: Open signup page
    signup.open()

    # Step 2: Basic signup
    signup.signup_basic(
        name="Vikrant Mankotia",
        email="sins5482@yopmail.com"
    )

    # Step 3: Account details
    signup.fill_account_details()

    # Step 4: Address details
    signup.fill_address_details()

    # Step 5: Submit
    signup.submit_account()

    # Assertion (basic validation)
    expect(page).to_have_url(re.compile("automationexercise"))

