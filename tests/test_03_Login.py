import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
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


def test_login(driver):
    page = LoginPage(driver)
    page.open()

    assert page.is_title_matches(), "Title does not match on homepage!"

    #Steps
    page.enter_user("tomsmith")  # ← missing
    page.enter_pass("SuperSecretPassword!")  # ← missing
    page.click_submit()

    time.sleep(3)                  # Wait for results to load

    #actual_title = driver.title.lower()
    logged_in_url = driver.current_url.lower()
    assert "secure" in logged_in_url, f"Expected 'secure' in url, but got '{logged_in_url}'"

    print("Test passed successfully!")


