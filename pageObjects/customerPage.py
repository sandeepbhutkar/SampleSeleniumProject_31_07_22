from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CustomerPage:

    btn_customer_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    btn_sub_customer_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btn_addnew_xpath = "//a[@class = 'btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    btn_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_link(self):
        self.driver.find_element(By.XPATH, self.btn_customer_xpath).click()


    def click_customer_sub_link(self):
        self.driver.find_element(By.XPATH,self.btn_sub_customer_xpath).click()

    def click_add_new_button(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def click_save(self):
        self.driver.find_element(By.NAME, self.btn_save_name).click()









