import allure
import pytest

from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..setting import USERNAME, PASSWORD, BASE_URL

inventory_link = BASE_URL + '/inventory.html'


@allure.suite('Inventory page tests')
@pytest.mark.inventory_page
class TestInventoryPage:
    @allure.title('Login before the actual test')
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.open(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        login_page.should_be_authorized_user()

    @allure.title('Open the inventory page')
    def test_user_can_open_inventory_page(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open(inventory_link)
        inventory_page.should_be_inventory_page()

    @allure.title('Add the product to cart')
    def test_user_can_see_count_of_items_in_cart(self, browser):
        inventory_page = InventoryPage(browser)
        inventory_page.open(inventory_link)
        inventory_page.click_button_with_text('Add to cart')
        inventory_page.should_be_items_count_on_cart_icon()

    @allure.title('Sort products by "{option_text}"')
    @pytest.mark.parametrize('option_text', [
        'Name (A to Z)',
        'Name (Z to A)',
        'Price (low to high)',
        'Price (high to low)'])
    def test_user_can_sort_products(self, browser, option_text):
        inventory_page = InventoryPage(browser)
        inventory_page.open(inventory_link)
        inventory_page.select_products_sorting_option_by_text(option_text)
        inventory_page.should_be_specific_active_sorting_option(option_text)
