from datetime import datetime

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page.BaseTool import BasePage
from testdata_files.test_data import ApplicationUrl


url = ApplicationUrl().webphone_url


class LoginHelper(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)

    def open_news(self):
            LOCATOR_SELECTOR = (By.XPATH, f"/html/body/div[3]/div/div[2]/div[5]/div[2]/div[2]/div[2]/a/span")
            self.find_element(LOCATOR_SELECTOR).click()
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            return self

    def check_title(self, title_data):
        with allure.step(f'check the team member tab'):
                LOCATOR_TITLE = (By.XPATH, f"/html/body/div[3]/div/div[1]/article/header/h1[text() = '{title_data}']")
                self.find_element(LOCATOR_TITLE)
                allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)


