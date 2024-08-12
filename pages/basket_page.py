from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_FORM)

    def should_be_text_about_empty(self):
        return self.is_element_present(*BasketPageLocators.BASKET_TEXT_EMPTY)
