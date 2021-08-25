import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--driver_name', action='store', default='chrome', help='Choose driver: chrome or firefox')
    parser.addoption('--language', action='store', default=None, help='Choose your language: ru, en, fr...')

# #as Chrome
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': 'language'})
#
# #as Firefox
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", 'language')

@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption('driver_name')
    driver_language = request.config.getoption('language')
    driver = None
    if driver_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': driver_language})
        print('\nStart driver Chrome...')
        driver = webdriver.Chrome(options=options)
    elif driver_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", driver_language)
        print('\nStart driver Firefox...')
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('\nEnd driver...')
    driver.quit()