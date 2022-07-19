import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from ..setting import BASE_WEBDRIVER_WAIT_TIMEOUT as TIMEOUT


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(TIMEOUT)

    @allure.step('Open the link {1}')
    def open(self, url):
        self.browser.get(url)

    @allure.step('Click on the button with text {1}')
    def click_button_with_text(self, text):
        locator = BasePageLocators.BUTTON_WITH_TEXT
        selector = (locator[0], locator[1].format(text))
        button = self.browser.find_element(*selector)
        button.click()

    @allure.step('Check that the text {1} is displayed on the page')
    def is_text_visible(self, text):
        xpath_string = xpath_prepare(text)
        try:
            WebDriverWait(self.browser, TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, xpath_string))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Check that the element found by the selector {2} is present on the page')
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Check if the element found by the selector {2} is not on the page')
    def is_element_not_present(self, how, what):
        try:
            WebDriverWait(self.browser, TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    @allure.step('Check that the element found by the selector {2} has disappeared within the timeout')
    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, TIMEOUT, 1, [TimeoutException]).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Check that the string {1} is present in the current URL')
    def is_substring_in_url_present(self, substring):
        if substring.lower() in self.browser.current_url:
            return True
        return False

    @allure.step('Check that the user is authorized')
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.LOGOUT_LINK), "Logout link is not presented," \
                                                                       " probably unauthorised user"


def xpath_prepare(search_text):
    """
    Helper function for case-insensitive search the text on the page
    @return: xpath string
    """
    return ".//*[contains(translate(., '$u', '$l'), '$s')]".replace("$u", search_text.upper()) \
        .replace("$l", search_text.lower()) \
        .replace("$s", search_text.lower())
