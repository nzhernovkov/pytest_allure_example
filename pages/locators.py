from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    BUTTON_WITH_TEXT = (By.XPATH, "//button[contains(text(), '{:s}')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login-box')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')


class InventoryPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '*[id^=add-to-cart]')
    ACTIVE_SORT_OPTION = (By.CSS_SELECTOR, '.active_option')
    CART_ICON = (By.CSS_SELECTOR, '#shopping_cart_container')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
    ITEM_CONTAINER = (By.CSS_SELECTOR, '.inventory_item')
    ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SORT_SELECTOR = (By.CSS_SELECTOR, '.product_sort_container')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '*[id^=remove]')


class CartPageLocators:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '#continue-shopping')
    CART_ITEM = (By.CSS_SELECTOR, '.cart_item')
    ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '*[id^=remove]')
