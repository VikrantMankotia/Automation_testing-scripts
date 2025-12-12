import sys
import os

# Add project root folder to Python path so 'pages' can be imported
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from pages.add_to_cart_page import AddToCartPage


def test_add_to_cart(page):
    add = AddToCartPage(page)

    # Step 1: Open website
    add.open()

    # Step 2: Login
    add.login()

    # Step 3: Add product
    add.add_product_to_cart()

    # Step 4: Verify cart page
    add.verify_cart()
