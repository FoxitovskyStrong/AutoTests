import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestQuestuin1():
    @pytest.mark.parametrize('link', [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ])
    def test_answer(self, driver, link):
        answer = math.log(int(time.time()))
        answer_text = str(answer)
        driver.get(link)
        driver.implicitly_wait(10)
        quiz = driver.find_element_by_class_name('string-quiz__textarea').send_keys(answer_text)
        botton = WebDriverWait(driver, 10)
        button_click = botton.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        button_click.click()
        driver.implicitly_wait(10)
        walt = WebDriverWait(driver, 10)
        text_correct = walt.until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        asserts = text_correct.text
        assert 'Correct!' == asserts
        print(asserts)
        time.sleep(1)
