from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini>span>a.btn")
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FIELD_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    FIELD_REPEAT_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGIESTER = (By.CSS_SELECTOR, "form#register_form>button.btn.btn-lg.btn-primary")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERT_INNER = (By.CSS_SELECTOR, "div.alertinner>strong")
    ALERT_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "div#messages>div.alert-success")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")

class BasketPageLocators:
    BASKET_ITEMS_FORM = (By.CSS_SELECTOR, "form#basket_formset")
    BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")
