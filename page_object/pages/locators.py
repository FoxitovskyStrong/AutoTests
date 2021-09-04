from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR,
	              '#login_link')
	LOGIN_LINK_IMVALID = (By.CSS_SELECTOR,
	                      '#login_link_error')


class LoginPageLocators():
	URL_LOGIN = (By.CSS_SELECTOR,
	             '$login_link')
	REGISTRATION_FORM = (By.CSS_SELECTOR,
	                     '#register_form')
	LOGIN_FORM = (By.CSS_SELECTOR,
	              '#login_form')


class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR,
	                 '.btn-add-to-basket')
	PRICE_TO_CART = (By.CSS_SELECTOR,
	                 '.basket-mini > strong')
	NAME_PRODUCT = (By.CSS_SELECTOR,
	                '.product_main > h1')
	ALERT_NAME = (By.CSS_SELECTOR,
	              '.alertinner > strong')
	PRODUCT_PRICE = (By.CSS_SELECTOR,
	                 '.product_main > .price_color')
	CART_PRICE = (By.CSS_SELECTOR,
	              '.alertinner p strong')
