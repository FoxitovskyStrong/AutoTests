import time

import pytest
link1 = 'http://suninjuly.github.io/registration1.html'


class TestRegistretionForms():
    @pytest.mark.parametrize('name, last, email', [
        pytest.param('Ivan', 'Ivanov', 'test@ya.ru'),
        pytest.param('Petr', 'Petrov', 'test2@ya.ru'),
        pytest.param('Sergey', 'Sergeev', 'test3@ya.ru')
    ])
    def test_first(self, driver, name, last, email):
        driver.get(link1)
        driver.implicitly_wait(5)
        first = driver.find_element_by_class_name('first').send_keys(name)
        lastName = driver.find_element_by_css_selector('.first_block > .second_class > .second').send_keys(last)
        email = driver.find_element_by_class_name("third").send_keys(email)
        button = driver.find_element_by_css_selector("button.btn").click()
        driver.implicitly_wait(5)
        confirm = driver.find_element_by_css_selector('.container > h1').text
        assert 'Congratulations! You have successfully registered!' == confirm
        time.sleep(3)