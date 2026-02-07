import pytest

from testdata.excelReader import ExcelReader

from Pages.loginPage import LoginPage

# Read Excel data
test_data = ExcelReader.read_login_data()


@pytest.mark.parametrize("Username,Password,Expected", test_data)
def test_login_ddt(page, Username, Password, Expected):

    login = LoginPage(page)

    login.login(Username, Password)

    if Expected == "success":

        assert "inventory.html" in page.url

    else:

        assert login.error.is_visible()