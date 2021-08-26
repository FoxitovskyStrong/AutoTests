from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,
                  '#login_link')

class LoginPageLocators():
    URL_LOGIN = (By.CSS_SELECTOR,
                 '$login_link')
    REGISTRATION_FORM = (By.CSS_SELECTOR,
                         '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR,
                  '#login_form')