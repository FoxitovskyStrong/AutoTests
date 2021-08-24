import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--driver_name', action='store', default=None, help='Choose driver: chrome or firefox')

@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption('driver_name')
    driver = None
    if driver_name == 'chrome':
        print('\nStart driver Chrome...')
        driver = webdriver.Chrome()
    elif driver_name == 'firefox':
        print('\nStart driver Firefox...')
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('\nEnd driver...')
    driver.quit()