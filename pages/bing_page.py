import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.bing_locators import BingLocators   # ← fixed import

class BingPage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://bing.com/"
        self.PAGE_TITLE = BingLocators.PAGE_TITLE
        self.SEARCH_BOX = BingLocators.SEARCH_BOX

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def is_title_matches(self):
        actual_title = self.get_title().strip()
        expected = "Search - Microsoft Bing"
        return expected in actual_title   # more flexible check

    def search(self, term):
        box = self.driver.find_element(By.ID, BingLocators.SEARCH_BOX)
        box.clear()
        box.send_keys(term)
        box.submit()
        #time.sleep(11)

