"""
Name : Test_LoginPage.py
Author : Jaga
Date : 12-02-2021
"""
import pytest
import allure

from pages.LoginPage import LoginPage
from tests.Test_BasePage import TestBase
from utilities.LoggingUtility import GenerateLogs
from utilities.ExcelUtility import ExcelReader
from utilities.FileReadUtility import ReadConfig


@allure.feature('Login Feature')
class TestLoginPage(TestBase):
    logger = GenerateLogs.log_gen(__name__)

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.story('Verify login button display')
    def test_verify_login_button(self):
        self.logger.info("Login page login button test execution start")
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.check_login_enabled()
        assert flag
        self.logger.info("Login page login button test execution end")

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.story('Verify login page title display')
    def test_login_page_title(self):
        self.logger.info("Login page title test execution start")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.get_login_page_title(ReadConfig.get_test_data('LOGIN_PAGE_TITLE'))
        self.logger.info("Login page title test execution end")

    @allure.story('Verify login functionality working fine')
    def test_login_to_application(self):
        self.logger.info("Login to application test execution start")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        self.logger.info("Login to application test execution end")

    @allure.story('Verify login functionality using data driven working fine')
    def test_login_to_application_by_excel_data(self):
        self.logger.info("Login to application using excel data test execution start")
        self.loginPage = LoginPage(self.driver)
        self.rows = ExcelReader.get_row_count(ReadConfig.get_test_data('EXCEL_FILE'), 'Login')
        print("Number of rows in a excel : ", self.rows)
        for row in range(2, self.rows + 1):
            self.username = ExcelReader.read_data(ReadConfig.get_test_data('EXCEL_FILE'), 'Login', row, 1)
            self.password = ExcelReader.read_data(ReadConfig.get_test_data('EXCEL_FILE'), 'Login', row, 2)
        self.loginPage.login_to_application(self.username, self.password)
        self.logger.info("Login to application using excel data test execution end")
