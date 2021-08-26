import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestFindButton():
    def test_find_shop_button(self, driver):
        driver.get(link)
        button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button')))
        button = len(driver.find_elements_by_css_selector('#add_to_basket_form > button'))
        assert button > 0, 'Button add to card not found!'
        time.sleep(15)
