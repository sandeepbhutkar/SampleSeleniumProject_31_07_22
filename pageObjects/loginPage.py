from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:

    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    btn_login_xpath = "//button[contains(text(),'Log in')]"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()





