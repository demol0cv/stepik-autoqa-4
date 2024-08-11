from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERT_INNER = (By.CSS_SELECTOR, "div.alertinner>strong")
    ALERT_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "div#messages>div.alert-success")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
