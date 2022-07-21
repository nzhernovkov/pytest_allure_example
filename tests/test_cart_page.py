import allure
import pytest

from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..resources.environment import USERNAME, PASSWORD


@allure.suite('Cart page tests')
@pytest.mark.cart_page
class TestCartPage:
    @allure.title('Login before the actual test')
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.open_this_page() \
            .login(USERNAME, PASSWORD) \
            .should_be_authorized_user()

    @allure.title('Add product to the cart before the actual test')
    @pytest.fixture
    def added_product(self, browser):
        inventory_page = InventoryPage(browser)
        name, price = inventory_page.open_this_page() \
            .click_add_to_cart_button_of_random_product_and_get_its_name_and_price()
        return name, price

    @allure.title('User can open the cart page')
    def test_user_can_open_cart_page(self, browser):
        cart_page = CartPage(browser)
        cart_page.open_this_page() \
            .should_be_cart_page()

    @allure.title('User can see added product in the cart')
    def test_user_can_see_product_in_cart(self, browser, added_product):
        cart_page = CartPage(browser)
        cart_page.open_this_page() \
            .should_be_added_item_in_cart(*added_product)

    @allure.title('User can remove added product from the cart')
    def test_user_can_remove_product_from_cart(self, browser, added_product):
        cart_page = CartPage(browser)
        cart_page.open_this_page() \
            .click_remove_button() \
            .should_not_be_items_in_cart()
