""" 
Name : HomePage.py
Author : Jaga
Date : 13-02-2021
"""
from pages.CustomerSearchPage import CustomerSearchPage
from reusableFunctions.PageHelper import PageHelper
from selenium.webdriver.common.by import By


class HomePage(PageHelper):
    text_dashboard_header = (By.CLASS_NAME, "content-header")
    text_account_name = (By.CLASS_NAME, "account-info")
    icon_settings = (By.XPATH, "//li[@class='dropdown']")
    left_nav_customers_option = (By.XPATH, "//a[@href='#']//span[text()='Customers']")
    left_nav_inline_customers_option = (By.XPATH, "//a[@href='/Admin/Customer/List']//span[text()='Customers']")
    add_new_button = (By.XPATH, "//a[@href='/Admin/Customer/Create']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_page_title(title)

    def get_home_dashboard_header(self):
        if self.verify_element_enable(self.text_dashboard_header):
            return self.get_element_text(self.text_dashboard_header)

    def check_settings_icon(self):
        return self.verify_element_enable(self.icon_settings)

    def get_account_name(self):
        if self.verify_element_enable(self.text_account_name):
            return self.get_element_text(self.text_account_name)

    def navigate_to_customer_search_page(self):
        self.element_click(self.left_nav_customers_option)
        self.element_click(self.left_nav_inline_customers_option)
        self.verify_element_enable(self.add_new_button)
        return CustomerSearchPage(self.driver)
