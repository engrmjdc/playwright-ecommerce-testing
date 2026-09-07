from playwright.sync_api import Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator('[data-test="title"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.product_prices = page.locator('[data-test="inventory-item-price"]')

    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def get_product_prices(self) -> list[float]:
        price_texts = self.product_prices.all_text_contents()

        return [float(price.replace("$", "")) for price in price_texts]
