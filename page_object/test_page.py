from pages.main_page import MainPage

def test_quest_can_to_do_main_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(driver):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()