import math
from selenium import webdriver
import time


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


urls = 'http://suninjuly.github.io/execute_script.html'

try:
	driver = webdriver.Chrome()
	driver.get(urls)

	txt = driver.find_element_by_xpath('//div//span[2]')
	txt_x = txt.text
	print(txt_x)
	math_x = calc(txt_x)
	driver.execute_script("window.scrollBy(0, 120);")

	answer = driver.find_element_by_id('answer').send_keys(math_x)

	checkbox = driver.find_element_by_css_selector('[type="checkbox"').click()

	robot = driver.find_element_by_id('robotsRule').click()
	time.sleep(1)

	submit = driver.find_element_by_tag_name('button').click()

finally:
	time.sleep(10)
	driver.close()
	driver.quit()
