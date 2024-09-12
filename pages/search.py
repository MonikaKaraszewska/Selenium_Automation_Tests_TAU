from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoSearchPage:
    URL = 'https://duckduckgo.com/'

    SEARCH_INPUT = (By.XPATH, "//input[@id='searchbox_input']")


    def __init__(self, browser: WebDriver):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)


    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)