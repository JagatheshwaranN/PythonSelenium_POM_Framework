""" 
Name : Test_CustomerSearchPage.py
Author : Jaga
Date : 27-02-2021
"""
import allure

from pages.HomePage import HomePage
from tests.Test_BasePage import TestBase
from pages.LoginPage import LoginPage
from utilities.LoggingUtility import GenerateLogs
from utilities.FileReadUtility import ReadConfig


@allure.feature('CustomerSearch Feature')
class TestCustomerSearchPage(TestBase):
    logger = GenerateLogs.log_gen(__name__)

    @allure.story('Verify customer search page title display')
    def test_verify_customer_search_page_title(self):
        self.logger.info("Customer search page title test execution start")
        self.loginPage = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        title = self.homepage.get_home_page_title(ReadConfig.get_test_data('HOME_PAGE_TITLE'))
        assert title == ReadConfig.get_test_data('HOME_PAGE_TITLE')
        customer_search_page = self.homepage.navigate_to_customer_search_page()
        title = customer_search_page.get_customer_search_page_title(ReadConfig.
                                                                    get_test_data('CUSTOMER_SEARCH_PAGE_TITLE'))
        assert title == ReadConfig.get_test_data('CUSTOMER_SEARCH_PAGE_TITLE')
        self.logger.info("Customer search page title test execution end")

    @allure.story('Verify customer search functionality working fine')
    def test_verify_customer_search_module(self):
        self.logger.info("Customer search module test execution start")
        self.loginPage = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        title = self.homepage.get_home_page_title(ReadConfig.get_test_data('HOME_PAGE_TITLE'))
        assert title == ReadConfig.get_test_data('HOME_PAGE_TITLE')
        customer_search_page = self.homepage.navigate_to_customer_search_page()
        title = customer_search_page.get_customer_search_page_title(ReadConfig.
                                                                    get_test_data('CUSTOMER_SEARCH_PAGE_TITLE'))
        assert title == ReadConfig.get_test_data('CUSTOMER_SEARCH_PAGE_TITLE')
        customer_search_page.validate_customer_search_module(ReadConfig.get_test_data('CUSTOMER_NAME'))
        self.logger.info("Customer search module test execution end")
