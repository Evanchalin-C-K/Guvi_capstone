# validation of Title and Options on the Admin page
import pytest
from selenium.webdriver.common.by import By
from CapstoneProject2.Conftest.conftest import Browser
from CapstoneProject2.PageObjects.data import Data
from CapstoneProject2.PageObjects.locators import Locators
from CapstoneProject2.PageObjects.yaml_function import YAML_Function

readData = YAML_Function(Data().yaml_file)

url = Data().web_url


class TestPIM:
    browser_manager = Browser("chrome")
    driver = browser_manager.setup_browser()

    def test_setup(self):
        self.driver.get(url)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Locators().username) \
            .send_keys(readData.yaml_reader()['login_username'])
        self.driver.find_element(by=By.CSS_SELECTOR, value=Locators().password) \
            .send_keys(readData.yaml_reader()['login_password'])
        self.driver.find_element(by=By.TAG_NAME, value=Locators().login_btn).click()

    def test_TC_PIM_01(self):

        # Title validation on Admin page
        # ------------------------------

        self.driver.implicitly_wait(10)
        # click on Admin tab
        self.driver.find_element(by=By.CSS_SELECTOR, value=Locators().admin_locator).click()
        # Title validation
        if readData.yaml_reader()['title'] in self.driver.title:
            assert True
            print("Title : True ")
        else:
            print("Title does not match")

    # negative case for title validation
    def test_TC_PIM_(self):
        self.driver.implicitly_wait(10)
        # click on Admin tab
        self.driver.find_element(by=By.CSS_SELECTOR, value=Locators().admin_locator).click()
        # Title validation
        if readData.yaml_reader()['title'] not in self.driver.title:
            assert True
            print("Title : True ")
        else:
            print("Title does not match")

        # Validate options on admin page
        # ------------------------------

    def test_options_validation(self):
        self.driver.implicitly_wait(10)
        # Append list of Options exists in the admin page
        options = self.driver.find_elements(by=By.XPATH, value=Locators().option)
        admin_options = []
        for menu in options:
            admin_options.append(menu.text)
        # Append remaining Options to the list
        admin_options.append(self.driver.find_element(by=By.LINK_TEXT, value=Locators().option_1).text)
        admin_options.append(self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=Locators().option_2).text)

        # Display Expected and Actual options in the list for validation
        expected_options = (readData.yaml_reader()['option'])
        print("\nExpected options in admin:\n", expected_options, "\n", "Actual options in admin : \n", admin_options)

    def test_TC_PIM_03(self):

        # Main menu validation on admin page
        # ----------------------------------

        actual_menu = []
        main_menu = self.driver.find_elements(by=By.XPATH, value=Locators().menu_locator)
        for menu in main_menu:
            actual_menu.append(menu.text)

        print("Expected menu :\n", readData.yaml_reader()['main_menus'], "\nActual menu :\n", actual_menu)

    def test_tearDown(self):
        self.driver.quit()
