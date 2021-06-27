from time import sleep
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()

    def find_element(self, locator, time=20):
        ignored_exception = StaleElementReferenceException, NoSuchElementException
        try:
            return WebDriverWait(self.driver, time, ignored_exceptions=ignored_exception).until(
                EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")
        except TimeoutError:
            print("TimeoutError is occurred")

    def wait(self, time):
        sleep(time)
        return self

    def refresh_page(self):
        self.driver.refresh()
        return self
