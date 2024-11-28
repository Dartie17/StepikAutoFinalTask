from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket is missing!"

    def items_card_should_not_be_in_empty_basket(self):
        assert self.is_element_not_present(*BasketPageLocators.BASKET_ITEMS_CARD), "Items card is present, but should not be"