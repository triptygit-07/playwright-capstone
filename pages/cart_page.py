class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_title = page.locator(".title")
        self.checkout_button = page.locator("#checkout")

    def get_cart_title(self):
        return self.cart_title.inner_text()

    def checkout(self):
        self.checkout_button.click()