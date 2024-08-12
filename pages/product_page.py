from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Add to basket button is not presented"  # noqa: E501

    def should_be_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGES), "Basket alert is not presented"

    def sould_not_be_basket_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGES), "Basket alert is presented"

    def should_not_be_success_alert(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_MESSAGES), "Basket alert is not disappeared"

    def add_to_basket(self):
        add_to_baske_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_baske_button.click()

    def product_title_equal_title_in_alert(self):
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_INNER).text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert alert_text == product_title, f"{alert_text} != {product_title}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGES), \
        "Success message is presented, but should not be"
