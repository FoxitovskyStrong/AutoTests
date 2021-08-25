import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):
        def test_registration_complited(self):
            link = "http://suninjuly.github.io/registration1.html"
            driver = webdriver.Chrome()
            driver.get(link)

            # Ваш код, который заполняет обязательные поля
            first = driver.find_element_by_class_name('first').send_keys('First')
            time.sleep(1)
            last = driver.find_element_by_class_name('second').send_keys('Last')
            time.sleep(1)
            email = driver.find_element_by_class_name("third").send_keys('Test@email.ru')
            time.sleep(1)
            # Отправляем заполненную форму
            button = driver.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = driver.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        def test_registration_failed(self):
            link = "http://suninjuly.github.io/registration2.html"
            driver = webdriver.Chrome()
            driver.get(link)

            # Ваш код, который заполняет обязательные поля
            first = driver.find_element_by_class_name('first').send_keys('First')
            time.sleep(1)
            last = driver.find_element_by_class_name('second').send_keys('Last')
            time.sleep(1)
            email = driver.find_element_by_class_name("third").send_keys('Test@email.ru')
            time.sleep(1)
            # Отправляем заполненную форму
            button = driver.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = driver.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

if __name__ == "__main__":
    unittest.main()