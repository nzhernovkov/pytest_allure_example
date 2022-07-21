import allure

from .base_page import BasePage
from .locators import LoginPageLocators
from ..resources.environment import LOGIN_URL


class LoginPage(BasePage):
    @allure.step('Open the Login page by url {url}')
    def open_this_page(self, url=LOGIN_URL):
        self.browser.get(url)

    @allure.step('Check that the current page is the login page')
    def should_be_login_page(self):
        self.should_be_login_form()

    @allure.step('Check that the user see the login error message')
    def should_see_login_error_message(self):
        assert self.is_text_visible("Epic sadface: Username and password do not match any user in this service"), \
            "Login error message is not present"

    @allure.step('Check that the login form present on the page')
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    @allure.step('Login with username - {1} and password - {2}')
    def login(self, username, password):
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        username_input.send_keys(username)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
