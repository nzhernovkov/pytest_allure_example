import allure
import pytest

from ..pages.login_page import LoginPage
from ..setting import USERNAME, PASSWORD, BASE_URL


@allure.suite('Login page tests')
@pytest.mark.login_page
class TestLoginPage:
    @allure.title('User can open the login page')
    def test_user_can_open_login_page(self, browser):
        login_page = LoginPage(browser)
        login_page.open(BASE_URL)
        login_page.should_be_login_page()

    @allure.title('User can login with valid credentials')
    def test_user_can_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        login_page.should_be_authorized_user()

    @allure.title('User can\'t login with invalid credentials')
    def test_user_can_not_login_with_invalid_login_data(self, browser):
        login_page = LoginPage(browser)
        login_page.open(BASE_URL)
        login_page.login('invalid_' + USERNAME, 'invalid_' + PASSWORD)
        login_page.should_see_login_error_message()
