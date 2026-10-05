import pytest
from pages.products_page import ProductsPage   
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage




@pytest.mark.smoke
def test_products_page_title(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    assert products_page.get_page_title() == "Products"



@pytest.mark.regression
def test_go_to_shopping_cart(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    products_page.go_to_shopping_cart()
    assert page.url.endswith("/cart.html")



@pytest.mark.regression
def test_go_to_cart(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.go_to_shopping_cart()

    assert "cart.html" in page.url

@pytest.mark.smoke
@pytest.mark.readonly
def test_products_are_displayed(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    backpack = page.get_by_text("Sauce Labs Backpack", exact=True)

    backpack.wait_for(state="visible")

    assert backpack.is_visible()




@pytest.mark.regression
def test_add_product_to_cart(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    add_to_cart = page.get_by_text("Add to cart", exact=True).first
    add_to_cart.click()

    cart_badge = page.locator(".shopping_cart_badge")

    assert cart_badge.inner_text() == "1"



@pytest.mark.regression
def test_remove_product_from_cart(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    add_to_cart = page.get_by_text("Add to cart", exact=True).first
    add_to_cart.click()

    cart_link = page.locator(".shopping_cart_link")
    cart_link.click()

    assert "cart.html" in page.url
    remove_button = page.get_by_text("Remove", exact=True)
    remove_button.click()

    assert page.get_by_text("Sauce Labs Backpack", exact=True).count() == 0


@pytest.mark.regression
def test_product_details(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    product = page.get_by_text("Sauce Labs Backpack", exact=True)
    product.click()

    assert "inventory-item.html" in page.url

    assert page.get_by_text("Sauce Labs Backpack", exact=True).is_visible()


@pytest.mark.regression
def test_sort_products(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    sort_dropdown = page.locator(".product_sort_container")
    sort_dropdown.select_option("lohi")
    prices = page.locator(".inventory_item_price").all_inner_texts()

    price_values = [float(price.replace("$", "")) for price in prices]

    assert price_values == sorted(price_values)



      