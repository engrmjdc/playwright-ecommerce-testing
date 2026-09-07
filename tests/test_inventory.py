from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_products_can_be_sorted_by_price_low_to_high(
    page: Page,
):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(InventoryPage.URL)

    inventory_page.sort_by_price_low_to_high()

    actual_prices = inventory_page.get_product_prices()
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices
