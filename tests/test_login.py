import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_user_can_log_in_with_valid_credentials(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "invalid_user",
            "invalid_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required",
        ),
    ],
)
def test_login_is_rejected_for_invalid_credentials(
    page: Page,
    username: str,
    password: str,
    expected_error: str,
):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)
    expect(page).to_have_url(LoginPage.URL)
