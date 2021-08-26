from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.URL_LOGIN), 'URL is not presented'
        login_link = self.driver.find_element(*LoginPageLocators.URL_LOGIN)
        login_link.click()
        assert 'login' in self.driver.current_url, 'URL is incorrect'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form from page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'No registration form from page'