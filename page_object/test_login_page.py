from pages.login_page import LoginPage


def test_guest_should_see_login_url(driver):
    link = 'http://selenium1py.pythonanywhere.com/fr/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_url()

def test_guest_should_see_login_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/fr/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_registration_form(driver):
    link = 'http://selenium1py.pythonanywhere.com/fr/accounts/login/'
    page = LoginPage(driver, link)
    page.open()
    page.should_be_register_form()