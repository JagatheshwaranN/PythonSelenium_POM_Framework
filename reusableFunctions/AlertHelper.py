"""
Name : AlertHelper.py
Author : Jaga
Date : 20-02-2021
"""


class AlertHelper:

    def __init__(self, driver):
        self.driver = driver

    def alert_accept(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.alert.dismiss()
