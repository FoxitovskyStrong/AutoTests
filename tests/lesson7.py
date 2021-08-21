import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

urls = 'http://suninjuly.github.io/selects1.html'

try:
	driver = webdriver.Chrome()
	driver.get(urls)

	num1 = driver.find_element_by_id('num1')
	num2 = driver.find_element_by_id('num2')

	s1 = num1.text
	s2 = num2.text

	summs = int(s1) + int(s2)

	select = Select(driver.find_element_by_tag_name("select"))
	select.select_by_value(str(summs))

	button = driver.find_element_by_css_selector('[type="submit"]').click()

finally:
	time.sleep(7)
	driver.close()
	driver.quit()