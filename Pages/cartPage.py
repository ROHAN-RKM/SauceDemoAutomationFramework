from utils.screenshot_helper import ScreenshotHelper


class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def open_cart(self):

        self.cart_icon.click()
        ScreenshotHelper.capture(self.page, "cart_open")

    def get_cart_items_count(self):

        ScreenshotHelper.capture(self.page, "cart_items_count")
        return self.cart_items.count()

    def go_to_checkout(self):

        self.checkout_button.click()
        ScreenshotHelper.capture(self.page, "cart_click_checkout")