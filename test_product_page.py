
import time

import pytest

from pages import LoginPage, ProductPage


@pytest.mark.need_review()
@pytest.mark.skip()
@pytest.mark.parametrize("link", ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
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
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_title_equal_title_in_alert()

@pytest.mark.need_review()
@pytest.mark.xfail()
@pytest.mark.parametrize("link", [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.sould_not_be_basket_alert()

@pytest.mark.need_review()
@pytest.mark.parametrize("link", [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.sould_not_be_basket_alert()

@pytest.mark.need_review()
@pytest.mark.xfail()
@pytest.mark.parametrize("link", [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_alert()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    raise NotImplementedError

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser, login_pair):
        link ="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        email = login_pair[0]
        password = login_pair[1]

        page.register_new_user(email, password)
        page.should_be_authorized_user()
        yield (email, password)
        print("Удаляем пользователя...")

    @pytest.mark.need_review()
    @pytest.mark.xfail()
    @pytest.mark.parametrize("link", [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.sould_not_be_basket_alert()

    @pytest.mark.need_review()
    @pytest.mark.parametrize("link", ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.product_title_equal_title_in_alert()

