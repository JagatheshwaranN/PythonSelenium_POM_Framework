"""
Name : Test_HomePage.py
Author : Jaga
Date : 13-02-2021
"""
import allure
import pytest
from pages.LoginPage import LoginPage
from tests.Test_BasePage import TestBase
from utilities.LoggingUtility import GenerateLogs
from utilities.FileReadUtility import ReadConfig


@allure.feature('HomePage Feature')
class TestHomePage(TestBase):
    logger = GenerateLogs.log_gen(__name__)

    @pytest.mark.regression
    @allure.story('Verify home page title display')
    def test_verify_home_page_title(self):
        self.logger.info("Home page title test execution start")
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        title = homepage.get_home_page_title(ReadConfig.get_test_data('HOME_PAGE_TITLE'))
        assert title == ReadConfig.get_test_data('HOME_PAGE_TITLE')
        self.logger.info("Home page title test execution end")

    @allure.story('Verify home page dashboard display')
    def test_verify_home_dashboard_header(self):
        self.logger.info("Home page dashboard test execution start")
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        dashboard_header = homepage.get_home_dashboard_header()
        assert dashboard_header == ReadConfig.get_test_data('DASHBOARD_HEADER')
        self.logger.info("Home page dashboard test execution end")

    @allure.story('Verify home page settings icon display')
    def test_verify_settings_icon(self):
        self.logger.info("Home page settings icon test execution start")
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        assert homepage.check_settings_icon()
        self.logger.info("Home page settings icon test execution end")

    @allure.story('Verify home page account name display')
    def test_verify_account_name(self):
        self.logger.info("Home page account test execution start")
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login_to_application(ReadConfig.get_username(), ReadConfig.get_password())
        account_name = homepage.get_account_name()
        assert account_name == ReadConfig.get_test_data('ACCOUNT_NAME')
        self.logger.info("Home page account test execution end")
