# Forget password link validation on login page
import time

import pytest

from CapstoneProject2.Conftest.conftest import Browser
from CapstoneProject2.PageObjects.data import Data
from CapstoneProject2.PageObjects.locators import Locators
from CapstoneProject2.PageObjects.yaml_function import YAML_Function
from selenium.webdriver.common.by import By

# read yaml data
readData = YAML_Function(Data().yaml_file)

url = Data().web_url
req_pwd_reset_link = Data().req_pwd_reset_url
sent_reset_pwd_link = Data().sent_reset_pwd_url


class TestForgetPassword:

    get_driver = Browser("chrome")
    driver = get_driver.setup_browser()

    @pytest.fixture
    def setup(self):
        self.driver.get(url)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Forget password link validation
    def test_tc_pim_01(self, setup):
        # click on forget password link
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Locators().forget_password).click()

        # validation of redirection to "request password reset" page
        if req_pwd_reset_link in self.driver.current_url:
            # validation of username texbox
            username_box = self.driver.find_element(by=By.XPATH, value=Locators().username_textbox)
            print("\nusername textbox visible :", username_box.is_displayed())
            # Enter the username in the username textbox
            username_box.send_keys(readData.yaml_reader()['username'])
            # click on reset password button
            self.driver.find_element(by=By.XPATH, value=Locators().reset_pwd_btn).click()
            # validation of reset password link
            if sent_reset_pwd_link in self.driver.current_url:
                time.sleep(5)
                self.driver.save_screenshot(Data().screenshot_path + "/forget_password.png")
                print("Password reset link sent successfully")




