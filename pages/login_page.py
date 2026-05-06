import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_locators import LoginLocators   # ← fixed import

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # ← add this
        self.URL = "https://the-internet.herokuapp.com/login"
        self.PAGE_TITLE = LoginLocators.PAGE_TITLE
        self.USERNAME = LoginLocators.USERNAME
        self.PASSWORD = LoginLocators.PASSWORD
        self.SUBMIT_BUTTON = LoginLocators.SUBMIT_BUTTON

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def is_title_matches(self):
        actual_title = self.get_title().strip()
        expected = "The Internet"
        return expected in actual_title   # more flexible check

    def enter_user(self, username):
        user = self.wait.until(EC.element_to_be_clickable((By.ID, self.USERNAME)))
        user.clear()
        user.send_keys(username)

    def enter_pass(self, password):
        pass_box = self.wait.until(EC.element_to_be_clickable((By.ID, self.PASSWORD)))
        pass_box.clear()
        pass_box.send_keys(password)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()



