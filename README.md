# Selenium Automation Testing with POM - Experimental Conftest Approaches

This repository demonstrates the use of the **Page Object Model (POM)** design pattern in **Selenium WebDriver** tests using **Python** and **pytest**. It also explores different ways of setting up test environments using `conftest.py`, showcasing how to implement parameterized tests and configure browsers dynamically.

## Features

- **Page Object Model (POM):**  
  Follows the POM design pattern for creating maintainable and reusable page classes for web automation.

- **Parameterized Tests with pytest:**  
  Dynamic testing for different browsers and input data with `@pytest.mark.parametrize`.

- **Multiple Test Setup Strategies:**  
  Exploring different methods of setting up and configuring Selenium WebDriver instances through:
  - `JSON_conftest.py`: Loads browser configuration from a JSON file.
  - `Lambda_conftest.py`: Uses a lambda function to dynamically select the browser (Chrome, Firefox, Edge).
  - `ORYconftest.py`: Placeholder for future advanced setup options.

- **Cross-browser Support:**  
  Tests support major browsers like **Chrome**, **Firefox**, and **Edge**, as well as **Headless Chrome** for CI/CD pipelines.

# Repository Structure

## `pages/`
Contains the Page Object Model files:

- `result.py` and `search.py`: Represent different web pages in the testing suite.

## `tests/`
Contains multiple testing strategies:

- `JSON_conftest.py`: Uses a JSON configuration file to dynamically load test settings.
- `Lambda_conftest.py`: Implements lambda functions to parametrize and configure WebDriver instances.
- `ORYconftest.py`: Placeholder for future conftest exploration.
- `test_search.py`: Example test using the DuckDuckGo search page object.

## `config.json`
A configuration file used to specify browser settings, implicitly waiting times, and other runtime parameters for `JSON_conftest.py`.


## Future Improvements

- Implementing the `ORYconftest.py` to further extend browser setup strategies.
- Adding real-world examples like login form automation and multi-page testing.
- CI/CD integration with GitHub Actions for automated test execution.

## Topics

- Selenium
- Python
- pytest
- Test Automation
- Page Object Model (POM)
- Cross-browser Testing
- Headless Browsers
- Continuous Integration (CI)
