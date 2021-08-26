from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        link_click = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link_click.click()
        # alert = self.driver.switch_to.alert
        # alert.accept()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK_IMVALID), 'Login link is not presented'
        # self.driver.find_element(By.CSS_SELECTOR, '#login_link_invalid')
