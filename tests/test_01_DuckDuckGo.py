import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.duckduckgo_page import DuckDuckGoPage


def test_duckduck_search(driver):
    page = DuckDuckGoPage(driver)
    page.open()

    assert page.is_title_matches(), "Title does not match on homepage!"

    page.search("Selenium")        # Make sure this actually types and submits

    time.sleep(3)                  # Wait for results to load

    actual_title = driver.title.lower()
    assert "selenium" in actual_title, f"Expected 'selenium' in title, but got '{actual_title}'"

    print("Test passed successfully!")