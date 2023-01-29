import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome, firefox, edge")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart browser Google Chrome for test...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        print("\nstart browser Firefox for test...")
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        print("\nstart browser Edge for test...")
        options = webdriver.EdgeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = EdgeService(EdgeChromiumDriverManager().install())
        browser = webdriver.Edge(service=service, options=options)
    else:
        print(f'Browser {browser_name} still is not implemented')
    browser.maximize_window()
    yield browser
    print("\nquit browser...")
    browser.quit()
