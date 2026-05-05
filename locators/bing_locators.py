# duckduckgo_locators.py
from selenium.webdriver.common.by import By


class BingLocators:
    # Better locator for page title (no full XPath)
    PAGE_TITLE = (By.TAG_NAME, "title")

    SEARCH_BOX = "sb_form_q"  # This is the actual input field