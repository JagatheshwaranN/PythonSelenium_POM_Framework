"""
Name : DropDownHelper.py
Author : Jaga
Date : 20-02-2021
"""

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from reusableFunctions.PageHelper import PageHelper
from selenium.webdriver.support.ui import Select


class DropDownHelper(PageHelper):

    def select_dropdown_value(self, by_locators, values):
        elements = self.get_locators(by_locators)
        if not values[0] == 'all':
            for option in elements:
                for value in range(len(values)):
                    if option.text == values[value]:
                        option.click()
                        break
        else:
            try:
                for option in elements:
                    time.sleep(1)
                    option.click()
            except Exception as ex:
                print(ex)

    def select_option_by_text(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        drop_down = Select(element)
        drop_down.select_by_visible_text(text)

    def select_option_by_value(self, by_locator, value):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        drop_down = Select(element)
        drop_down.select_by_value(value)

    def select_option_by_index(self, by_locator, index):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        drop_down = Select(element)
        drop_down.select_by_index(index)