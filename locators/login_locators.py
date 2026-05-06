# duckduckgo_locators.py
from selenium.webdriver.common.by import By


class LoginLocators:
    # Better locator for page title (no full XPath)
    PAGE_TITLE = (By.TAG_NAME, "title")

    USERNAME = "username"  # This is the actual input field
    PASSWORD = "password"
    SUBMIT_BUTTON = (By.TAG_NAME, "button")
