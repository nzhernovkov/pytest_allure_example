import allure
import pytest

from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..resources.environment import USERNAME, PASSWORD, SORTING_OPTIONS


@allure.suite('Inventory page tests')
@pytest.mark.inventory_page
class TestInventoryPage:
    @allure.title('Login before the actual test')
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.open_this_page() \
            .login(USERNAME, PASSWORD) \
            .should_be_authorized_user()

    @allure.title('User can open the inventory page')
    def test_user_can_open_inventory_page(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open_this_page() \
            .should_be_inventory_page()

    @allure.title('User can see count of added products on the cart icon')
    def test_user_can_see_count_of_products_on_cart_icon(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open_this_page() \
            .click_add_to_cart_button() \
            .should_be_items_count_on_cart_icon()

    @allure.title('User can remove added products from the cart')
    def test_user_can_remove_products_from_cart(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open_this_page() \
            .click_add_to_cart_button() \
            .should_be_remove_button() \
            .click_remove_button() \
            .should_not_be_remove_button()

    @allure.title('User can go to the cart page from the inventory page by clicking on the cart icon')
    def test_user_can_go_to_cart_from_inventory(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open_this_page() \
            .click_cart_icon()
        cart_page = CartPage(browser)
        cart_page.should_be_cart_page()

    @allure.title('User can sort products by "{sorting_option}" with filter')
    @pytest.mark.parametrize(*SORTING_OPTIONS)
    def test_user_can_sort_products_with_filter(self, browser, sorting_option):
        inventory_page = InventoryPage(browser)
        inventory_page.open_this_page() \
            .select_products_sorting_option_by_text(sorting_option) \
            .should_be_specific_active_sorting_option(sorting_option)
