import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.duckduckgo_page import DuckDuckGoPage


@pytest.fixture
def driver():
    options = Options()
    # Check if we are running in a Jenkins environment
    is_jenkins = os.getenv('JENKINS_URL') is not None

    if is_jenkins:
        print("Detected Jenkins: Forcing Headless Mode")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        print("Detected Local Environment: Opening Browser Window")
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_duckduck_search(driver):
    page = DuckDuckGoPage(driver)
    page.open()

    # Pytest uses asserts to report status to Jenkins
    assert page.is_title_matches(), "Title does not match on homepage!"

    page.search("Selenium")

    actual_title = driver.title.lower()
    assert "selenium" in actual_title, f"Expected 'selenium' in title, but got '{actual_title}'"