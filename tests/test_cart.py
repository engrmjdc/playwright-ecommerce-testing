from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_user_can_add_multiple_products_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.open_cart()

    expect(page).to_have_url(CartPage.URL)
    expect(cart_page.cart_items).to_have_count(2)
    expect(cart_page.product_names).to_have_text(
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
        ]
    )
    expect(cart_page.product_quantities).to_have_text(["1", "1"])


def test_user_can_remove_product_from_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(2)

    cart_page.remove_backpack()

    expect(cart_page.cart_items).to_have_count(1)
    expect(cart_page.product_names).to_have_text(["Sauce Labs Bike Light"])
    expect(inventory_page.cart_badge).to_have_text("1")
