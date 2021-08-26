import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_card(self):
        self.should_be_to_add()
        self.should_be_to_math()
        self.should_be_to_price_card()

    def should_be_to_add(self):
        to_card = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET)
        to_card.click()
        time.sleep(1)