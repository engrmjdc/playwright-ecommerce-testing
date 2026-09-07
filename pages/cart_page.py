from playwright.sync_api import Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.product_quantities = page.locator('[data-test="item-quantity"]')
        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        # Inside __init__
        self.checkout_button = page.locator('[data-test="checkout"]')

    def remove_backpack(self):
        self.remove_backpack_button.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()
