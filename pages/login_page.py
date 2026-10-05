class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username, password):

        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

        if username == "standard_user" and password == "secret_sauce":
            self.page.wait_for_url("**/inventory.html")
            self.page.wait_for_timeout(2000)