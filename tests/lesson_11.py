from selenium import webdriver
import time
import os

link_site = 'http://suninjuly.github.io/file_input.html'

try:
	driver = webdriver.Chrome()
	driver.get(link_site)
	name = driver.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')
	lastname = driver.find_element_by_css_selector('[name="lastname"]').send_keys('Petrov')
	email = driver.find_element_by_css_selector('[name="email"]').send_keys('ivan_petrov@ya.ru')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'test.txt')
	download = driver.find_element_by_css_selector('[name="file"]').send_keys(file_path)
	button = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
	time.sleep(5)
	driver.close()
	driver.quit()
