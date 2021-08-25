from selenium import webdriver
import time
import pytest

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

@pytest.fixture(scope='class')
def driver():
    print('\nStart driver...')
    driver = webdriver.Chrome()
    yield driver
    print('\nClose driver...')
    driver.quit()


class TestRegistration():
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_RegistrationCase1(self, driver):
        driver.get(link1)
        first = driver.find_element_by_class_name('first').send_keys('First')
        driver.implicitly_wait(3)
        last = driver.find_element_by_css_selector('.first_block > .second_class > .second').send_keys('Last')
        driver.implicitly_wait(3)
        email = driver.find_element_by_class_name("third").send_keys('Test@email.ru')
        driver.implicitly_wait(3)
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        driver.implicitly_wait(5)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        time.sleep(3)
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!", welcome_text

    @pytest.mark.xfail
    def test_RegistrationCase2(self, driver):
        driver.get(link2)
        first = driver.find_element_by_class_name('first').send_keys('First')
        driver.implicitly_wait(3)
        last = driver.find_element_by_css_selector('.first_block > .second_class > .second').send_keys('Last')
        driver.implicitly_wait(3)
        email = driver.find_element_by_class_name("third").send_keys('Test@email.ru')
        driver.implicitly_wait(3)
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        driver.implicitly_wait(5)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        time.sleep(5)
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!", welcome_text