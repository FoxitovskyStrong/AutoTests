import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
	def should_be_add_to_card(self):
		self.should_be_to_add()
		self.solve_quiz_and_get_code()
		self.should_be_name_to_product_and_alert()
		self.should_be_card_and_product_price()

	def should_be_to_add(self):
		to_card = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET)
		to_card.click()

	def should_be_name_to_product_and_alert(self):
		name = self.driver.find_element(*ProductPageLocators.NAME_PRODUCT).text
		alert_name = self.driver.find_element(*ProductPageLocators.ALERT_NAME).text
		assert alert_name == name

	def should_be_card_and_product_price(self):
		price_product = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		price_cart = self.driver.find_element(*ProductPageLocators.CART_PRICE).text
		print(price_cart)
		assert price_product == price_cart, 'Price cart != price product'
