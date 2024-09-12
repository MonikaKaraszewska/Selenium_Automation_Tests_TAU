import time

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver.remote.webdriver import WebDriver  # to jest po to zeby mi podopowiadalo metody
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize('phrase', ['panda', 'python', 'giant panda'])
@pytest.mark.usefixtures("initialize_driver")  # do lmbda i headless conftest
# def test_basic_duckduckgo_search(browser: WebDriver): #i to (browser: WebDriver), do JSON_conftest
def test_basic_duckduckgo_search(initialize_driver: WebDriver, phrase):

    # do JSON conftest
    search_page = DuckDuckGoSearchPage(initialize_driver)
    result_page = DuckDuckGoResultPage(initialize_driver)

    # search_page = DuckDuckGoSearchPage(browser)
    # result_page = DuckDuckGoResultPage(browser)

    # phrase = 'python'

    search_page.load()

    search_page.search(phrase)
    WebDriverWait(initialize_driver, 10).until(EC.title_contains(phrase))
    assert phrase in result_page.title()
    # print("NO I Co;",result_page.search_input_value())
    assert (phrase == result_page.search_input_value())


    titles = result_page.result_link_titles()
    titles2 = titles[0]
    print("TITLES2: ", titles2)
    # WebDriverWait(initialize_driver,10).until(EC.presence_of_element_located(result_page.RESULT_lINKS))

    # matches = [t for t in titles2 if phrase in t]
    # print('Matches: ', matches)
    # # print('ciekawe ile: ',len(matches))
    # assert len(matches) > 0

    """alternatywa z lista"""
    # phrases = ['Panda', 'panda', 'PANDA', 'Pandka', 'pandzie', 'pandy']
    # panda_title_list = []
    # for title in titles2:
    #     for panda in phrases:
    #         if panda in title:
    #             panda_title_list.append(title)
    # # print('ilepandow', len(panda_title_list))
    # # print('pandalist', panda_title_list)
    # assert len(panda_title_list) > 0

    # '''zamiana tytulow na male litery'''
    panda_title_list_lower = []
    for title in titles2:
        t = title.lower()
        if phrase in t:
            panda_title_list_lower.append(t)
    # print('Panda lower list: ', panda_title_list_lower)
    # print('dlugosc Panda lower list: ', len(panda_title_list_lower()))
    assert len(panda_title_list_lower) > 0
