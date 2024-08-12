from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not contain login/"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        raise NotImplementedError

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        raise NotImplementedError

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL)
        pass1 = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD)
        pass2 = self.browser.find_element(*LoginPageLocators.FIELD_REPEAT_PASSWORD)
        reg_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGIESTER)

        email_field.send_keys(email)
        pass1.send_keys(password)
        pass2.send_keys(password)
        reg_button.click()
