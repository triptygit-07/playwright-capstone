import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage


DATA_FILE = Path(__file__).resolve().parents[2] / "test_data" / "login_data.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    INVALID_LOGIN_DATA = json.load(file)


@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

    page.wait_for_url("**/inventory.html")

    assert "inventory" in page.url


@pytest.mark.regression
@pytest.mark.parametrize(
    "login_data",
    INVALID_LOGIN_DATA
)
def test_invalid_login(page, login_data):

    login_page = LoginPage(page)

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    assert "inventory" not in page.url

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert "Epic sadface" in error_message.inner_text()