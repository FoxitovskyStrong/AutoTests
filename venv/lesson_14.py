import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
	driver = webdriver.Chrome()
	driver.get(link)
	price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
	book = driver.find_element_by_id('book').click()
	input_value = driver.find_element_by_id('input_value')
	x = input_value.text
	math_x = calc(x)
	answer = driver.find_element_by_id('answer').send_keys(math_x)
	solve = driver.find_element_by_id('solve').click()
finally:
	time.sleep(6)
	driver.close()
	driver.quit()
