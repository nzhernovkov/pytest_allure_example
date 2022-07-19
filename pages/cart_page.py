import allure

from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    @allure.step('Check that the current page is the cart page')
    def should_be_cart_page(self):
        self.should_be_cart_page_texts()
        self.should_be_checkout_button()
        self.should_be_continue_shopping_button()

    @allure.step('Check that page texts present on the page')
    def should_be_cart_page_texts(self):
        assert self.is_text_visible("Your Cart"), "\"Your Cart\" text is not present"
        assert self.is_text_visible("DESCRIPTION"), "\"DESCRIPTION\" text is not present"
        assert self.is_text_visible("QTY"), "\"QTY\" text is not present"

    @allure.step('Check that the "Checkout" button present on the page')
    def should_be_checkout_button(self):
        assert self.is_element_present(*CartPageLocators.CHECKOUT_BUTTON), "Checkout button is not present"

    @allure.step('Check that the "Continue Shopping" button present on the page')
    def should_be_continue_shopping_button(self):
        assert self.is_element_present(*CartPageLocators.CONTINUE_SHOPPING_BUTTON), \
            "Continue Shopping button is not present"

    @allure.step('Check that an item present in the cart')
    def should_be_item_in_cart(self):
        assert self.is_element_present(*CartPageLocators.CART_ITEM), "Item is not present in the cart"

    @allure.step('Check that an item not present in the cart')
    def should_not_be_item_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), "Item is present in the cart"

    @allure.step('Click on the "Remove" button')
    def click_remove_button(self):
        button = self.browser.find_element(*CartPageLocators.REMOVE_BUTTON)
        button.click()