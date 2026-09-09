import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_user_can_complete_checkout(
    authenticated_page: Page,
):
    page = authenticated_page
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()

    expect(page).to_have_url(CheckoutPage.INFORMATION_URL)

    checkout_page.enter_customer_information(
        first_name="Mack",
        last_name="Dela Cruz",
        postal_code="1000",
    )
    checkout_page.continue_to_overview()

    expect(page).to_have_url(CheckoutPage.OVERVIEW_URL)

    checkout_page.finish_order()

    expect(page).to_have_url(CheckoutPage.COMPLETE_URL)
    expect(checkout_page.complete_message).to_have_text("Thank you for your order!")


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        (
            "",
            "Dela Cruz",
            "1000",
            "Error: First Name is required",
        ),
        (
            "Mack",
            "",
            "1000",
            "Error: Last Name is required",
        ),
        (
            "Mack",
            "Dela Cruz",
            "",
            "Error: Postal Code is required",
        ),
    ],
)
def test_checkout_rejects_missing_customer_information(
    authenticated_page: Page,
    first_name: str,
    last_name: str,
    postal_code: str,
    expected_error: str,
):
    page = authenticated_page
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()

    expect(page).to_have_url(CheckoutPage.INFORMATION_URL)

    checkout_page.enter_customer_information(
        first_name=first_name,
        last_name=last_name,
        postal_code=postal_code,
    )
    checkout_page.continue_to_overview()

    expect(checkout_page.error_message).to_have_text(expected_error)
    expect(page).to_have_url(CheckoutPage.INFORMATION_URL)
