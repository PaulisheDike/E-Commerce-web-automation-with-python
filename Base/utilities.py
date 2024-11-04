from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from configTest import BaseUrl


class Utilities:

    def __init__(self, driver):
        self.driver = driver

    def type_something(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def click_something(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    # def is_visible(self, locator):
    #     return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).is_displayed()

    def is_visible(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False



