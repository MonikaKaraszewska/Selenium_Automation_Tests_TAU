from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DuckDuckGoResultPage:

    RESULT_lINKS = (By.XPATH, "//a[@data-testid='result-title-a']")
    SEARCH_INPUT_RESULT_PAGE = (By.ID,'search_form_input')

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_lINKS)
        titles = [link.text for link in links]
        return[titles]

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_RESULT_PAGE)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title