import pytest
from selenium import webdriver
from endpoints import Endpoints



@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    driver.get(Endpoints.URL_MAIN)
    yield driver
    driver.quit()


