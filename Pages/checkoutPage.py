from utils.screenshot_helper import ScreenshotHelper


class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.first_Name = page.get_by_placeholder("First Name")
        self.last_Name = page.get_by_placeholder("Last Name")
        self.zip_pincode = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("[data-test='continue']")

    def fill_options(self):

        self.first_Name.fill("Rohan")
        ScreenshotHelper.capture(self.page, "checkout_first_name")

        self.last_Name.fill("Mishra")
        ScreenshotHelper.capture(self.page, "checkout_last_name")

        self.zip_pincode.fill("700056")
        ScreenshotHelper.capture(self.page, "checkout_zip")

    def continue_to_Payment(self):

        self.continue_button.click()
        ScreenshotHelper.capture(self.page, "checkout_continue")