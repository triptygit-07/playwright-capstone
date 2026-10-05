class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.page_title = page.locator(".title")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def get_page_title(self):
        return self.page_title.text_content()

    def go_to_shopping_cart(self):
        self.shopping_cart_link.click() 

