import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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