from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
import pytest
#>pytest -v -m smoke --html=C:/Users/san/PycharmProjects/NopCommerce/reports/report_31_07_2022.html test_verify_title.py

class Test_Verify_Title:

    @pytest.mark.smoke
    def test_TC001_verify_title(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/san/PycharmProjects/Driver/chromedriver.exe")
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        lp = LoginPage(self.driver)
        lp.enter_email("admin@yourstore.com")
        lp.enter_password("admin")
        lp.click_login_button()

        self.title = self.driver.title
        if self.title == "Dashboard / nopCommerce administration1":
            assert True
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file("C:/Users/san/PycharmProjects/NopCommerce/screenshot/titleFail.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_TC002_verify_title(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/san/PycharmProjects/Driver/chromedriver.exe")
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        lp = LoginPage(self.driver)
        lp.enter_email("admin@yourstore.com")
        lp.enter_password("admin")
        lp.click_login_button()

        self.title = self.driver.title
        if self.title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file("C:/Users/san/PycharmProjects/NopCommerce/screenshot/titleFail.png")
            self.driver.close()
            assert False


