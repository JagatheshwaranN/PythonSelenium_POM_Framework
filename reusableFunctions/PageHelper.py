"""
Name : PageHelper.py
Author : Jaga
Date : 12-02-2021
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageHelper:

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, by_locator):
        return self.driver.find_element(by_locator)

    def get_locators(self, by_locator):
        return self.driver.find_elements(by_locator)

    def element_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).click()

    def element_clear(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).clear()

    def enter_text_into_element(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title1):
        WebDriverWait(self.driver, 30).until(ec.title_is(title1))
        return self.driver.title
