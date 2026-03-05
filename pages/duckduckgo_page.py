import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.duckduckgo_locators import DuckDuckGoLocators   # ← fixed import

class DuckDuckGoPage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://duckduckgo.com/"
        self.PAGE_TITLE = DuckDuckGoLocators.PAGE_TITLE

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def is_title_matches(self):
        actual_title = self.get_title().strip()
        expected = "DuckDuckGo - Protection. Privacy. Peace of mind."
        return expected in actual_title   # more flexible check

    def search(self, term):
        box = self.driver.find_element(By.ID, "searchbox_input")
        box.clear()
        box.send_keys(term)
        box.send_keys(Keys.RETURN)
        #time.sleep(11)

