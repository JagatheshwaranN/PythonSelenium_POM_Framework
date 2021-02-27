""" 
Name : LoginPage.py
Author : Jaga
Date : 12-02-2021
"""
from pages.HomePage import HomePage
from reusableFunctions.PageHelper import PageHelper
from selenium.webdriver.common.by import By
from utilities.FileReadUtility import ReadConfig


class LoginPage(PageHelper):
    textbox_email = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_login = (By.XPATH, "//input[@value='Log in']")
    link_logout = (By.XPATH, "//a[@href='/logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ReadConfig.get_application_url())

    def get_login_page_title(self, title1):
        return self.get_page_title(title1)

    def check_login_enabled(self):
        return self.verify_element_enable(self.button_login)

    def login_to_application(self, username, password):
        self.element_clear(self.textbox_email)
        self.enter_text_into_element(self.textbox_email, username)
        self.element_clear(self.textbox_password)
        self.enter_text_into_element(self.textbox_password, password)
        self.element_click(self.button_login)
        # self.verify_element_enable(self.link_logout)
        # self.element_click(self.link_logout)
        return HomePage(self.driver)
