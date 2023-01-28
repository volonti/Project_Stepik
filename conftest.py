import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()
