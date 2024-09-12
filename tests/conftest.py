from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    global driver
    if request.param == "chrome":
        opts = Options()
        opts.add_argument('--headless')
        # opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        driver = webdriver.Chrome(options=opts)
    elif request.param == "firefox":
        opts = Options()
        opts.add_argument('--headless')
        driver = webdriver.Firefox(options=opts)
    elif request.param == "edge":
        opts = Options()
        opts.add_argument('--headless')
        driver = webdriver.Edge(options=opts)
    print("Browser:", request.param)

    driver.implicitly_wait(10)
    yield driver
    print("Close Driver")
    driver.quit()