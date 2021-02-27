"""
Name : MouseActionHelper.py
Author : Jaga
Date : 20-02-2021
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from reusableFunctions.PageHelper import PageHelper


class MouseActionHelper(PageHelper):

    def __init__(self, driver):
        self.driver = driver

    def element_double_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def element_drag_drop(self, by_locator1, by_locator2):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator1))
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator2))
        draggable_element = self.get_locator(by_locator1)
        droppable_element = self.get_locator(by_locator2)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable_element, droppable_element).perform()

    def element_right_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        element = self.get_locator(by_locator)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def element_hover(self, by_locator1, by_locator2):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator1))
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator2))
        parent_element = self.get_locator(by_locator1)
        child_element = self.get_locator(by_locator2)
        actions = ActionChains(self.driver)
        actions.move_to_element(parent_element).move_to_element(child_element).click().perform()




