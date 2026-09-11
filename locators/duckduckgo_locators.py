# duckduckgo_locators.py
from selenium.webdriver.common.by import By


class DuckDuckGoLocators:
    # Better locator for page title (no full XPath)
    PAGE_TITLE = (By.TAG_NAME, "title")

    # We'll add the search box next
    SEARCH_BOX = (By.NAME, "q")  # DDG's search field ID—stable