from utils.screenshot_helper import ScreenshotHelper


class FinalPage:

    def __init__(self, page):
        self.page = page
        self.final_Button = page.get_by_role("button", name="Finish")

    def click_final_button(self):

        self.final_Button.click()
        ScreenshotHelper.capture(self.page, "final_click_finish")