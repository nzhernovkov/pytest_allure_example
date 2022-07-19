import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from allure_commons.types import AttachmentType


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
        driver.set_page_load_timeout(30)
        driver.maximize_window()
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(options=options)
        print("\nstart firefox browser for test..")
        driver.set_page_load_timeout(30)
        driver.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    return driver


@pytest.fixture(scope="function")
def browser(request, driver):
    yield driver
    # Make screenshot if test fails
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=request.function.__name__,
            attachment_type=AttachmentType.PNG
        )
    print("\nquit browser..")
    driver.quit()
