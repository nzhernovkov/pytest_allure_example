import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from ..resources.selenium_configs import IMPLICITLY_TIMEOUT, WAIT_FOR_TIMEOUT


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(IMPLICITLY_TIMEOUT)

    @allure.step('Open the link "{url}"')
    def open(self, url):
        self.browser.get(url)

    @allure.step('Click on the button with text "{text}"')
    def click_button_with_text(self, text):
        locator = BasePageLocators.BUTTON_WITH_TEXT
        formatted_locator = (locator[0], locator[1].format(text))
        button = self.browser.find_element(*formatted_locator)
        button.click()

    @allure.step('Check that the text "{text}" is displayed on the page')
    def is_text_visible(self, text):
        xpath_string = xpath_prepare(text)
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, xpath_string))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Check that the element found by "{how}" with the selector "{what}" is present on the page')
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Check that the element found by "{how}" with the selector "{what}" is not present on the page')
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    @allure.step('Check that the user is authorized')
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.LOGOUT_LINK), "Logout link is not present," \
                                                                       " probably unauthorised user"


def xpath_prepare(search_text):
    """
    Helper function for case-insensitive search the text on the page
    @return: xpath string
    """
    return ".//*[contains(translate(., '$u', '$l'), '$s')]".replace("$u", search_text.upper()) \
        .replace("$l", search_text.lower()) \
        .replace("$s", search_text.lower())
