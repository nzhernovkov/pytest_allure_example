from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    BUTTON_WITH_TEXT = (By.XPATH, "//button[contains(text(), '{0}')]")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login-box')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')


class InventoryPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_ICON = (By.CSS_SELECTOR, '#shopping_cart_container')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '*[id^=add-to-cart]')
    SORT_SELECTOR = (By.CSS_SELECTOR, '.product_sort_container')
    ACTIVE_SORT_OPTION = (By.CSS_SELECTOR, '.active_option')
