import allure

from resources.environment import CART_URL
from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    @allure.step('Open the "Cart" page by url {url}')
    def open_this_page(self, url=CART_URL):
        self.browser.get(url)
        return self

    @allure.step('Check that the current page is the cart page')
    def should_be_cart_page(self):
        self.should_be_cart_page_texts()
        self.should_be_checkout_button()
        self.should_be_continue_shopping_button()
        return self

    @allure.step('Check that page texts present on the page')
    def should_be_cart_page_texts(self):
        assert self.is_text_visible("Your Cart"), "\"Your Cart\" text is not present"
        assert self.is_text_visible("DESCRIPTION"), "\"DESCRIPTION\" text is not present"
        assert self.is_text_visible("QTY"), "\"QTY\" text is not present"
        return self

    @allure.step('Check that the "Checkout" button present on the page')
    def should_be_checkout_button(self):
        assert self.is_element_present(*CartPageLocators.CHECKOUT_BUTTON), "Checkout button is not present"
        return self

    @allure.step('Check that the "Continue Shopping" button present on the page')
    def should_be_continue_shopping_button(self):
        assert self.is_element_present(*CartPageLocators.CONTINUE_SHOPPING_BUTTON), \
            "Continue Shopping button is not present"
        return self

    @allure.step('Check that added item present in the cart')
    def should_be_added_item_in_cart(self, name, price):
        self.should_match_product_name(name)
        self.should_match_product_price(price)
        return self

    @allure.step('Check that the name of added product in the cart matches its name in the inventory')
    def should_match_product_name(self, inventory_name):
        name = self.browser.find_element(*CartPageLocators.ITEM_NAME).text
        assert name == inventory_name, \
            f"Cart product name '{inventory_name}' not match inventory product name '{name}"
        return self

    @allure.step('Check that the price of added product in the cart matches its price in the inventory')
    def should_match_product_price(self, inventory_price):
        price = self.browser.find_element(*CartPageLocators.ITEM_PRICE).text
        assert price == inventory_price, \
            f"Cart product price '{inventory_price}' not match inventory product price '{price}'"
        return self

    @allure.step('Check that an item not present in the cart')
    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), "Item is present in the cart"
        return self

    @allure.step('Click on the "Remove" button')
    def click_remove_button(self):
        button = self.browser.find_element(*CartPageLocators.REMOVE_BUTTON)
        button.click()
        return self
