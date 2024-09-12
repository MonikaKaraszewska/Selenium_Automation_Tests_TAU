import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    b = webdriver.Chrome()

    b.implicitly_wait(10)

    yield b

    b.quit()