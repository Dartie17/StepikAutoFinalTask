from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MERCH_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MERCH_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_TO_BASKET_TEXT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")