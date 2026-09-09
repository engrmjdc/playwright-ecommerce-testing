from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


def test_products_can_be_sorted_by_price_low_to_high(
    authenticated_page: Page,
):
    inventory_page = InventoryPage(authenticated_page)

    inventory_page.sort_by_price_low_to_high()

    actual_prices = inventory_page.get_product_prices()
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices