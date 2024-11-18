from .pages.product_page import ProductPage


def test_merch_adds_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_added_in_basket_merch_name()
    page.should_be_right_basket_price()