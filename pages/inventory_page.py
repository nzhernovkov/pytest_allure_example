import random

import allure

from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .locators import InventoryPageLocators
from ..resources.environment import INVENTORY_URL


class InventoryPage(BasePage):
    @allure.step('Open the Inventory page by url {url}')
    def open_this_page(self, url=INVENTORY_URL):
        self.browser.get(url)

    @allure.step('Check that the current page is the inventory page')
    def should_be_inventory_page(self):
        self.should_be_cart_icon()
        self.should_be_add_to_cart_button()

    @allure.step('Check that the cart icon present on the page')
    def should_be_cart_icon(self):
        assert self.is_element_present(*InventoryPageLocators.CART_ICON), "Cart icon is not present"

    @allure.step('Check that the "Add to cart" button present on the page')
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*InventoryPageLocators.ADD_TO_CART_BUTTON), \
            "Add to cart button is not present"

    @allure.step('Check that the "Remove" button present on the page')
    def should_be_remove_button(self):
        assert self.is_element_present(*InventoryPageLocators.REMOVE_BUTTON), "Remove button is not present"

    @allure.step('Check that the "Remove" button not present on the page')
    def should_not_be_remove_button(self):
        assert self.is_not_element_present(*InventoryPageLocators.REMOVE_BUTTON), "Remove button is present"

    @allure.step('Check that count of items shown on the cart icon')
    def should_be_items_count_on_cart_icon(self):
        assert self.is_element_present(*InventoryPageLocators.CART_BADGE), \
            "Count of items not present on the cart icon"

    @allure.step('Check that active sorting option is "{option_text}"')
    def should_be_specific_active_sorting_option(self, option_text):
        active_option_text = self.browser.find_element(*InventoryPageLocators.ACTIVE_SORT_OPTION).text
        assert active_option_text.lower() == option_text.lower(), \
            f"Actual active option text is \"{active_option_text}\", expected \"{option_text}\""

    @allure.step('Select sorting products by text {option_text}')
    def select_products_sorting_option_by_text(self, option_text):
        select = Select(self.browser.find_element(*InventoryPageLocators.SORT_SELECTOR))
        select.select_by_visible_text(option_text)

    @allure.step('Click on the cart icon')
    def click_cart_icon(self):
        link = self.browser.find_element(*InventoryPageLocators.CART_ICON)
        link.click()

    @allure.step('Click on the "Add to cart" button')
    def click_add_to_cart_button(self):
        button = self.browser.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    @allure.step('Click on the "Add to Cart" button of a random product and get its name and price.')
    def click_add_to_cart_button_of_random_product_and_get_its_name_and_price(self):
        items = self.browser.find_elements(*InventoryPageLocators.ITEM_CONTAINER)
        random_item = items[random.randrange(0, len(items))]
        button = random_item.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        name = random_item.find_element(*InventoryPageLocators.ITEM_NAME).text
        price = random_item.find_element(*InventoryPageLocators.ITEM_PRICE).text
        return name, price

    @allure.step('Click on the "Remove" button')
    def click_remove_button(self):
        button = self.browser.find_element(*InventoryPageLocators.REMOVE_BUTTON)
        button.click()
