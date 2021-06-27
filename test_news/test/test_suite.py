import allure
import pytest

from testdata_files.test_data import *


@allure.title('news')
@pytest.mark.regression
@pytest.mark.news
def test_check_news(browser):
    d = Data()
    page_news = browser
    page_news.open_news()
    page_news.check_title(d.title)