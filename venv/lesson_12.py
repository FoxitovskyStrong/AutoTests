import math
from selenium import webdriver
import time


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
	driver = webdriver.Chrome()
	driver.get(link)
	button_1 = driver.find_element_by_css_selector('[type="submit"]').click()
	confirm = driver.switch_to.alert
	confirm.accept()
	nums = driver.find_element_by_id('input_value')
	calcs = nums.text
	calcs_result = calc(calcs)
	answer = driver.find_element_by_css_selector('[name="text"]').send_keys(calcs_result)
	button = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
	time.sleep(5)
	driver.close()
	driver.quit()

