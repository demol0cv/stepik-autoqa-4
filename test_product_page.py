
import pytest

from pages.product_page import ProductPage

@pytest.mark.skip
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, timeout=0)
    page.open()
    # assert page.browser.current_url == link, "Bug here"
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    code = page.solve_quiz_and_get_code()
    page.product_title_equal_title_in_alert()


@pytest.mark.parametrize('link', [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.sould_not_be_basket_alert()
    # page.solve_quiz_and_get_code()
    
@pytest.mark.parametrize('link', [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.sould_not_be_basket_alert()

@pytest.mark.parametrize('link', [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_alert()
