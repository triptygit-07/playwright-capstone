import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



@pytest.mark.regression
def test_checkout_from_cart(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.go_to_shopping_cart()

    cart_page = CartPage(page)
    cart_page.checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_information(
        "John",
        "Doe",
        "94087"
    )

    checkout_page.continue_checkout()

    finish_button = page.get_by_text("Finish", exact=True)
    finish_button.click()
    page.wait_for_url("**/checkout-complete.html")
    page.wait_for_timeout(2000)

    assert "checkout-complete.html" in page.url

    confirmation = page.get_by_text(
        "Thank you for your order!",
        exact=True
    )

   
    assert confirmation.is_visible()

   