import time
from pages.eventwizz_signup import SignupPage


def test_vendor_signup(page):
    signup = SignupPage(page)

    # Open signup page
    signup.open_signup_page()

    # Generate unique email
    timestamp = int(time.time())
    email = f"vendor{timestamp}@yopmail.com"

    # Perform signup
    signup.signup_with_email(email)

    print(f"Signup flow executed with email: {email}")
