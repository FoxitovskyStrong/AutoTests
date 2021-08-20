import math
from selenium import webdriver
import time


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
	driver = webdriver.Chrome()
	driver.get(link)
	button_1 = driver.find_element_by_css_selector('[type="submit"]').click()
	new_window = driver.window_handles[1]
	driver.switch_to.window(new_window)
	nums = driver.find_element_by_id('input_value')
	nums_int = nums.text
	nums_result = calc(nums_int)
	answer = driver.find_element_by_css_selector('[name="text"]').send_keys(nums_result)
	button_2 = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
	time.sleep(5)
	driver.close()
	driver.quit()
