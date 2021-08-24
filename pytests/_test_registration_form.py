import time
import pytest

link1 = 'http://suninjuly.github.io/registration1.html'

class TestRegistretionForms():
    def test_first(self, driver):
        driver.get(link1)
        first = driver.find_element_by_class_name('first')

    @pytest.mark.xfail(reason='fixing this bug right now', strict='False')
    def test_last(self, driver):
        driver.get(link1)
        last = driver.find_element_by_css_selector('.first_block > .second_class > .second')

    def test_email(self, driver):
        driver.get(link1)
        email = driver.find_element_by_class_name("third")

    def test_button(self, driver):
        driver.get(link1)
        button = driver.find_element_by_css_selector("button.btn")
