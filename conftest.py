import pytest
from selenium import webdriver
from curl import *
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.set_preference("credentials_enable_service", False)
    options.set_preference("profile.password_manager_enabled", False)
    options.set_preference("profile.password_manager_leak_detection", False)
    driver = webdriver.Firefox(options=options)
    driver.get(main_page)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def order_page_driver(driver):
    driver.get(order_page)
    return driver
