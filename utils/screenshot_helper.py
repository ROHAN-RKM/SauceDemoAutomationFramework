import os
import datetime


class ScreenshotHelper:

    screenshot_dir = None   # will be set dynamically per test run

    @staticmethod
    def set_screenshot_dir(test_name):

        base_dir = "screenshots"

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        folder_name = f"{test_name}_{timestamp}"

        full_path = os.path.join(base_dir, folder_name)

        os.makedirs(full_path)

        ScreenshotHelper.screenshot_dir = full_path

        return full_path


    @staticmethod
    def capture(page, step_name):

        if ScreenshotHelper.screenshot_dir is None:
            raise Exception("Screenshot directory not set")

        timestamp = datetime.datetime.now().strftime("%H%M%S")

        file_name = f"{step_name}_{timestamp}.png"

        file_path = os.path.join(ScreenshotHelper.screenshot_dir, file_name)

        page.screenshot(path=file_path)

        print(f"Screenshot saved: {file_path}")