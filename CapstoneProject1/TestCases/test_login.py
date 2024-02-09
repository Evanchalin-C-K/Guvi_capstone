# Test Login
import time

import pytest

from CapstoneProject2.Conftest.conftest import Browser
from selenium.webdriver.common.by import By
from CapstoneProject1.PageObjects.data import Data
from CapstoneProject1.PageObjects.excel_function import Excel_Function
from CapstoneProject1.PageObjects.locators import Locators


class TestLogin:
    url = Data().web_url
    excel_file = Data().excel_file
    sheet_num = Data().sheet_number

    # Get the row count of Excel file
    s = Excel_Function(excel_file, sheet_num)
    rows = s.row_count()

    get_driver = Browser("chrome")
    driver = get_driver.setup_browser()

    # test setup - to Launch the browser
    @pytest.fixture
    def setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_login(self, setup):
        # retrieve the username and password from the Excel file
        for row in range(2, self.rows+1):
            username = self.s.read_file(row, 4)
            print(username)
            password = self.s.read_file(row, 5)
            print(password)

            # Login with username and password
            self.driver.find_element(by=By.NAME, value=Locators().username_locator).send_keys(username)
            self.driver.find_element(by=By.NAME, value=Locators().password_locator).send_keys(password)
            self.driver.find_element(by=By.XPATH, value=Locators().login_button).click()

            # validation for Successful login
            if Data().dashboard_url in self.driver.current_url:
                print("Success : LOGIN WITH USERNAME {a}, PASSWORD {b}".format(a=username, b=password))
                # Capture Screenshot of successful login
                time.sleep(10)
                self.driver.save_screenshot(Data().screenshot_path + "/login_success{c}.png".format(c=row-1))
                # write test result to the file
                self.s.write_file(row, 6, "TEST PASSED")
                # Logout
                self.driver.find_element(by=By.XPATH, value=Locators().logout_dropdown).click()
                self.driver.find_element(by=By.LINK_TEXT, value=Locators().logout_button).click()

            # Unsuccessful Login with the username and password
            elif self.url in self.driver.current_url:
                print("Failed : LOGIN WITH USERNAME {a}, PASSWORD {b}".format(a=username, b=password))
                # Capture Screenshot of unsuccessful login
                time.sleep(10)
                self.driver.save_screenshot(Data().screenshot_path + "/login_failed{c}.png".format(c=row-1))
                # write test result to the file
                self.s.write_file(row, 6, "TEST FAILED")


