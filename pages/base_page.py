from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, time=30):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def check_element_is_clickable(self, locator, time=30):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def click_to_element(self, locator, time=30):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        self.driver.get(url)

    def url_to_be(self, url, time=30):
        return WebDriverWait(self.driver, time).until(expected_conditions.url_to_be(url))

    def drag_and_drop(self, what, where):
        drag = self.find_element_with_wait(what)
        drop = self.find_element_with_wait(where)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()


