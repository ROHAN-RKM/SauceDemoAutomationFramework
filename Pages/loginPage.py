from utils.screenshot_helper import ScreenshotHelper


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def login(self, username, password):

        self.username_input.fill(username)
        ScreenshotHelper.capture(self.page, "login_enter_username")

        self.password_input.fill(password)
        ScreenshotHelper.capture(self.page, "login_enter_password")

        self.login_button.click()
        ScreenshotHelper.capture(self.page, "login_click_button")