from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_user_can_complete_checkout(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

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
