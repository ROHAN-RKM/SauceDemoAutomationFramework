from utils.screenshot_helper import ScreenshotHelper


class InventoryPage:

    def __init__(self, page):
        self.page = page
        product_name = "Sauce Labs Bike Light"

        product_row = page.locator(".inventory_item").filter(has_text=product_name)

        self.add_to_cart_button = product_row.get_by_role("button", name="Add to cart")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self):

        self.add_to_cart_button.click()
        ScreenshotHelper.capture(self.page, "inventory_add_item")

    def get_cart_count(self):

        ScreenshotHelper.capture(self.page, "inventory_cart_count")
        return self.cart_badge.inner_text()