import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestLanguage():
    def test_language_and_botton_shop(self, driver):
        driver.get(link)
        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button')))
        button = len(driver.find_elements_by_css_selector('#add_to_basket_form > button'))
        assert button > 0, 'Button add to card not found!'
        time.sleep(15)