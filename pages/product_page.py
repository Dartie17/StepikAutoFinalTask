from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def find_merch_name(self):
        return self.find_text(*ProductPageLocators.MERCH_NAME)

    def find_merch_price(self):
        return self.find_text(*ProductPageLocators.MERCH_PRICE)

    def find_added_to_basket_merch_name(self):
        return self.find_text(*ProductPageLocators.ADDED_TO_BASKET_TEXT)

    def find_basket_price(self):
        return self.find_text(*ProductPageLocators.BASKET_PRICE)

    def should_be_right_added_in_basket_merch_name(self):
        assert self.find_merch_name() == self.find_added_to_basket_merch_name(), "Merch name in message is wrong!"

    def should_be_right_basket_price(self):
        assert self.find_merch_price() == self.find_basket_price(), "Basket price is not equals merch price!"