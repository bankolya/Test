from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import pytest
from page_objects.Login_Page import LoginHelper
import allure

def pytest_addoption(parser):
    parser.addoption("--cmdoptbrowser", action="store", default="chrome", help="my option: chrome or firefox")


@pytest.fixture(scope='function')
def cmdoptbrowser(request):
    return request.config.getoption("--cmdoptbrowser")


@pytest.fixture(scope="function")
def browser(cmdoptbrowser):
    if cmdoptbrowser == "firefox":
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   desired_capabilities=firefox_capabilities)
        yield LoginHelper(driver)
        driver.quit()
    elif cmdoptbrowser == "chrome":
        chrome_capabilities = webdriver.DesiredCapabilities.CHROME
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  desired_capabilities=chrome_capabilities)
        yield LoginHelper(driver)
        try:
            allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
        driver.quit()
