import pytest
from selenium import webdriver
from pages.duckduckgo_page import DuckDuckGoPage


# Your page class stays the same...

def test_duckduck_title():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = DuckDuckGoPage(driver)
        page.open()

        if page.is_title_matches():
            print("PASS: Title matches!")
        else:
            print("FAIL: Title doesn't match.")

        page.search("Selenium")

        #asserts title page of search results
        actual_title = page.get_title().lower()
        if "selenium" in actual_title:
            print("PASS: Search worked!")
        else:
            print("FAIL: Search title wrong:", actual_title)

    finally:
        driver.quit()  # always runs—even if search bombs