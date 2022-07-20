import allure
import pytest

from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..resources.environment import BASE_URL, CART_URL, INVENTORY_URL, USERNAME, PASSWORD


@allure.suite('Cart page tests')
@pytest.mark.cart_page
class TestCartPage:
    @allure.title('Login before the actual test')
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.open(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        login_page.should_be_authorized_user()

    @allure.title('Add product to the cart before the actual test')
    @pytest.fixture
    def add_product_to_cart(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open(INVENTORY_URL)
        inventory_page.click_add_to_cart_button()

    @allure.title('User can open the cart page')
    def test_user_can_open_cart_page(self, browser):
        cart_page = CartPage(browser)
        cart_page.open(CART_URL)
        cart_page.should_be_cart_page()

    @allure.title('User can see added product in the cart')
    def test_user_can_see_product_in_cart(self, browser, add_product_to_cart):
        cart_page = CartPage(browser)
        cart_page.open(CART_URL)
        cart_page.should_be_item_in_cart()

    @allure.title('User can remove added product from the cart')
    def test_user_can_remove_product_from_cart(self, browser, add_product_to_cart):
        cart_page = CartPage(browser)
        cart_page.open(CART_URL)
        cart_page.click_remove_button()
        cart_page.should_not_be_item_in_cart()
