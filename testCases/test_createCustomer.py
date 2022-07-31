from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pageObjects.customerPage import CustomerPage
from pageObjects.loginPage import LoginPage
from utilities import XLutils

path = "C:/Users/san/PycharmProjects/NopCommerce/testData/testData.xlsx"
row = XLutils.get_row_count(path, "Sheet1")

class Test_Nop_Commerce:
    def test_createCustomer(self):
        # open browser
        for r in range(2, row + 1):
            self.driver = webdriver.Chrome(executable_path="C:/Users/san/PycharmProjects/Driver/chromedriver.exe")
            self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
            self.driver.maximize_window()
            # login page
            self.lp = LoginPage(self.driver)
            self.lp.enter_email("admin@yourstore.com")
            self.lp.enter_password("admin")
            self.lp.click_login_button()
            # add new customer
            self.cp = CustomerPage(self.driver)
            self.cp.click_customer_link()
            self.cp.click_customer_sub_link()
            self.cp.click_add_new_button()
            self.cp.enter_email(XLutils.read_data(path, "Sheet1", r, 2))
            self.cp.enter_password(XLutils.read_data(path, "Sheet1", r, 3))
            self.cp.enter_firstname(XLutils.read_data(path, "Sheet1", r, 4))
            self.cp.enter_lastname(XLutils.read_data(path, "Sheet1", r, 5))
            self.cp.click_save()

            # copy customer number
            self.copy = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Customers')]")
            print(self.copy.text)
            XLutils.write_data(path, "Sheet1", r, 6, self.copy.text)
            # close browser
            time.sleep(2)
            self.driver.close()




