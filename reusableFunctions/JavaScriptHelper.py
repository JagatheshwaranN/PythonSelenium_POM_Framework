"""
Name : JavaScriptHelper.py
Author : Jaga
Date : 20-02-2021
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from reusableFunctions.PageHelper import PageHelper


class JavaScriptHelper(PageHelper):

    def js_element_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        self.driver.execute_script("arguments[0].click()", element)

    def js_get_page_title(self):
        self.driver.implicitly_wait(10)
        title = self.driver.execute_script("return document.title")
        return title

    def js_scroll_to_element(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_page_refresh(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("history.go(0);")

    def js_page_scroll_up(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

    def js_page_scroll_down(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def js_open_tab(self):
        self.driver.execute_script("window.open()")

