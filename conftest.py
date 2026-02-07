import os
import sys

# This line forces the project root into Python's search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
import os
import pytest
from playwright.sync_api import sync_playwright
from utils.screenshot_helper import ScreenshotHelper

@pytest.fixture(scope="function")
def page(request):

    # Create screenshot folder per test
    ScreenshotHelper.set_screenshot_dir(request.node.name)

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://www.saucedemo.com/")

        yield page

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":

        page = item.funcargs.get("page", None)

        if page:

            status = "PASS" if report.passed else "FAIL"

            timestamp = datetime.datetime.now().strftime("%H%M%S")

            file_name = f"FINAL_{status}_{timestamp}.png"

            file_path = os.path.join(
                ScreenshotHelper.screenshot_dir,
                file_name
            )

            page.screenshot(path=file_path)

            print(f"\nFinal Screenshot saved: {file_path}")