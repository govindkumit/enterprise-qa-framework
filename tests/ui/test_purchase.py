import pytest
from config.config import BASE_URL
from test_data.users import STANDARD_USER

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_purchase(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    print("Opened:", driver.current_url)

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    print("After login:", driver.current_url)

    # Products
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    print("Product added")

    products_page.open_cart()

    print("After cart click:", driver.current_url)

    # Cart
    cart_page = CartPage(driver)

    cart_page.checkout()

    print("After checkout click:", driver.current_url)

    # Checkout
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_customer_details(
        "Govi",
        "QA",
        "560001"
    )

    checkout_page.continue_checkout()

    checkout_page.complete_order()

    message = checkout_page.get_confirmation_message()

    assert message == "Thank you for your order!"