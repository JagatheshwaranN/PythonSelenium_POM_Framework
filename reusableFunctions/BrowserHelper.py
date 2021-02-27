"""
Name : BrowserHelper.py
Author : Jaga
Date : 20-02-2021
"""


class BrowserHelper:

    def __init__(self, driver):
        self.driver = driver

    def page_back(self):
        self.driver.implicitly_wait(5)
        self.driver.back()

    def page_forward(self):
        self.driver.implicitly_wait(5)
        self.driver.forward()
