import allure
import pytest

from resources.environment import USERNAME, PASSWORD


@allure.suite('Login page tests')
@pytest.mark.login_page
class TestLoginPage:
    @allure.title('User can open the login page')
    def test_user_can_open_login_page(self, login_page):
        login_page.open_this_page() \
            .should_be_login_page()

    @allure.title('User can login with valid credentials')
    def test_user_can_login(self, login_page):
        login_page.open_this_page() \
            .login(USERNAME, PASSWORD) \
            .should_be_authorized_user()

    @allure.title('User can\'t login with invalid credentials')
    def test_user_can_not_login_with_invalid_login_data(self, login_page):
        login_page.open_this_page().login('invalid_' + USERNAME, 'invalid_' + PASSWORD) \
            .should_see_login_error_message()
