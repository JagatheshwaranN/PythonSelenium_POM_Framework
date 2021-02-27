"""
Name : conftest.py
Author : Jaga
Date : 13-02-2021
"""
import allure
import pytest
from allure_commons.types import AttachmentType

from utilities.FileReadUtility import ReadConfig
from selenium import webdriver
from datetime import datetime

pass_screenshot_folder = "screenshots/pass/"
fail_screenshot_folder = "screenshots/fail/"


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    return report


@pytest.fixture(scope="function")
def init_driver(request):
    driver = webdriver.Chrome(executable_path=ReadConfig.get_test_data('CHROME_DRIVER_PATH'))
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield driver
    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=AttachmentType.PNG)
        take_screenshot(driver, request.node.name, fail_screenshot_folder)
    elif request.node.rep_call.passed:
        take_screenshot(driver, request.node.name, pass_screenshot_folder)
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=AttachmentType.PNG)
    driver.quit()


def take_screenshot(driver, test_name, path):
    file_name = path+f'{test_name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'
    driver.save_screenshot(file_name)
