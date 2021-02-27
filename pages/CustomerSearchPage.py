""" 
Name : CustomerSearchPage.py
Author : Jaga
Date : 27-02-2021
"""

from reusableFunctions.PageHelper import PageHelper
from selenium.webdriver.common.by import By
from utilities.LoggingUtility import GenerateLogs


class CustomerSearchPage(PageHelper):
    logger = GenerateLogs.log_gen(__name__)

    textbox_firstname = (By.ID, "SearchFirstName")
    button_customer_search = (By.ID, "search-customers")
    customer_search_section = (By.XPATH, "//div[@class='panel panel-default panel-search']")
    table_customer_grid = (By.XPATH, "//table[@id='customers-grid']")
    table_customer_grid_name = (By.XPATH, "//table[@id='customers-grid']//tbody//tr//td[3]")
    table_customer_grid_empty = (By.XPATH, "//table//td[@class='dataTables_empty']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_customer_search_page_title(self, title):
        return self.get_page_title(title)

    def validate_customer_search_module(self, customer_name):
        self.verify_element_enable(self.customer_search_section)
        self.enter_text_into_element(self.textbox_firstname, customer_name)
        self.element_click(self.button_customer_search)
        flag = self.verify_element_enable(self.table_customer_grid)
        if flag is True:
            self.logger.info("Customer search result section found")
            flag = self.verify_element_enable(self.table_customer_grid_name)
            if flag is True:
                actual_customer_name = self.get_element_text(self.table_customer_grid_name)
                if actual_customer_name.__eq__("Victoria Terces"):
                    self.logger.info("Customer match successful")
                    assert True
                else:
                    self.logger.info("Customer match unsuccessful")
                    assert False
            else:
                self.logger.info("No Customer data found")
                self.verify_element_enable(self.table_customer_grid_empty)
                assert False
        else:
            self.logger.info("No customer search result section found")
            assert False
