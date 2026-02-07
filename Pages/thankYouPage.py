from utils.screenshot_helper import ScreenshotHelper


class ThankYouPage:

    def __init__(self, page):
        self.page = page
        self.homePage_button = page.get_by_role("button", name="Back Home")

    def back_to_home(self):

        ScreenshotHelper.capture(self.page, "thank_you_page")

        self.homePage_button.click()

        ScreenshotHelper.capture(self.page, "back_to_home")