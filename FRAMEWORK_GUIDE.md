# Python + Selenium Test Framework
### A Developer's Reference Guide
*Page Object Model | pytest | Jenkins CI/CD | Allure Reporting*

---

## 1. Environment Setup

### 1.1 Install Python
- Download Python 3.14+ from [python.org](https://python.org)
- During install, check **Add Python to PATH**
- Verify: `python --version`

### 1.2 Install Required Packages
```bash
pip install selenium pytest allure-pytest webdriver-manager
```
Or install from requirements.txt:
```bash
pip install -r requirements.txt
```
**requirements.txt:**
```
selenium
pytest
allure-pytest
webdriver-manager
```

### 1.3 Install Chrome Browser
- Install Google Chrome (latest stable)
- ChromeDriver is managed automatically via `webdriver-manager`
- For Jenkins/headless: Chrome must be installed on the agent machine

### 1.4 Project Folder Structure
```
selenium-py/
├── tests/
│   ├── __init__.py
│   ├── test_01_DuckDuckGo.py
│   ├── test_02_Bing.py
│   └── test_03_Login.py
├── pages/
│   ├── duckduckgo_page.py
│   ├── bing_page.py
│   └── login_page.py
├── locators/
│   ├── duckduckgo_locators.py
│   ├── bing_locators.py
│   └── login_locators.py
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## 2. Page Object Model (POM) Overview

The Page Object Model is a design pattern that separates test logic from page interaction logic. Each web page gets its own class, making tests cleaner, more readable, and easier to maintain.

Every page in this framework is represented by three files:

| File | Location | Purpose |
|------|----------|---------|
| Locator file | `locators/` | Stores all element selectors (IDs, CSS, XPath) |
| Page file | `pages/` | Contains actions and interactions for that page |
| Test file | `tests/` | Contains the test steps, fixture, and assertions |

---

## 3. Locator File

### Purpose
The locator file stores all element selectors in one place. When the UI changes, you only update the locator file — not every test that uses that element.

### What Goes In It
- Class constants for each element on the page
- Uses Selenium's By strategies: `By.ID`, `By.CSS_SELECTOR`, `By.XPATH`, `By.TAG_NAME`
- Store selectors as tuples (By strategy, value) for direct use in waits

### Example
```python
from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME      = (By.ID, "username")
    PASSWORD      = (By.ID, "password")
    SUBMIT_BUTTON = (By.TAG_NAME, "button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
```

---

## 4. Page File

### Purpose
The page file contains all the actions a user can take on that page. It imports the locators and uses Selenium WebDriver to interact with elements. Tests call these methods rather than using WebDriver directly.

### Key Components

**`__init__` (Constructor)**
- Accepts the driver instance from the test fixture
- Sets up `WebDriverWait` for explicit waits
- Defines the page URL
- Maps locators from the locator class to instance variables

**Action Methods**
- `open()` — navigates to the page URL
- `enter_user(username)` — types into the username field
- `enter_pass(password)` — types into the password field
- `click_submit()` — clicks the submit button
- `is_logout_visible()` — returns True if logout button is displayed

### Example
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.URL           = "https://the-internet.herokuapp.com/login"
        self.USERNAME      = LoginLocators.USERNAME
        self.PASSWORD      = LoginLocators.PASSWORD
        self.SUBMIT_BUTTON = LoginLocators.SUBMIT_BUTTON
        self.LOGOUT_BUTTON = LoginLocators.LOGOUT_BUTTON

    def open(self):
        self.driver.get(self.URL)

    def enter_user(self, username):
        field = self.wait.until(EC.element_to_be_clickable(self.USERNAME))
        field.clear()
        field.send_keys(username)

    def enter_pass(self, password):
        field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        field.clear()
        field.send_keys(password)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def is_logout_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        ).is_displayed()
```

---

## 5. Test File

### Purpose
The test file contains the pytest fixture (browser setup/teardown) and the actual test functions. It imports the page class and calls action methods in sequence, then asserts the expected outcome.

### Key Components

**pytest Fixture**
- Decorated with `@pytest.fixture`
- Sets up Chrome options (headless for Jenkins, windowed locally)
- Detects Jenkins vs local via `JENKINS_URL` environment variable
- Yields the driver to the test, then quits after the test completes

**Test Function**
- Function name must start with `test_`
- Accepts the driver fixture as a parameter
- Creates a page object instance
- Calls page methods in order (open, interact, assert)
- Uses `assert` statements to validate expected behavior

### Example
```python
import os, time, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    is_jenkins = os.getenv('JENKINS_URL') is not None

    if is_jenkins:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login(driver):
    page = LoginPage(driver)
    page.open()

    assert page.is_title_matches(), "Title mismatch!"

    page.enter_user("tomsmith")
    page.enter_pass("SuperSecretPassword!")
    page.click_submit()

    time.sleep(3)

    logged_in_url = driver.current_url.lower()
    assert "secure" in logged_in_url, f"Login failed. URL: {logged_in_url}"
    print("Test passed successfully!")
```

---

## 6. Explicit Waits

Never use `time.sleep()` as your primary wait strategy. Explicit waits are faster and more reliable — they proceed as soon as the condition is met.

| Condition | Use When |
|-----------|----------|
| `element_to_be_clickable` | Clicking buttons, links, or input fields |
| `visibility_of_element_located` | Asserting an element is visible on screen |
| `presence_of_element_located` | Element exists in DOM but may not be visible |
| `text_to_be_present_in_element` | Waiting for specific text to appear |

---

## 7. Running Tests

```bash
# Run all tests
pytest tests/

# Run a specific test
pytest tests/test_03_Login.py::test_login

# Run with JUnit output (for Jenkins)
pytest tests/ --junitxml=results.xml

# Run with Allure reporting
pytest tests/ --alluredir=allure-results
```

---

## 8. Jenkins CI/CD

### Pipeline Stages
- **Checkout SCM** — checks out the repo from source control
- **Install Dependencies** — creates venv and runs pip install
- **Run Tests** — activates venv and runs pytest with JUnit and Allure flags
- **Post Actions** — publishes JUnit and Allure reports

### Headless Mode Detection
```python
is_jenkins = os.getenv('JENKINS_URL') is not None
```
When running in Jenkins, Chrome launches in headless mode with `--no-sandbox` and `--disable-dev-shm-usage` flags required for CI environments.

### Required Jenkins Plugins
- Pipeline
- JUnit Plugin
- Allure Plugin

---

## 9. Allure Reporting

### Install
```bash
pip install allure-pytest
```

### Run with Allure
```bash
pytest tests/ --alluredir=allure-results
```

### Jenkinsfile Post Section
```groovy
post {
    always {
        junit 'results.xml'
        allure includeProperties: false, jdk: '',
               results: [[path: 'allure-results']]
    }
}
```

---

## 10. Best Practices

| Practice | Why |
|----------|-----|
| Use explicit waits | More reliable than `sleep()`; proceeds as soon as element is ready |
| Keep credentials in the test | Page class handles interactions, not data |
| Store locators as tuples | Pass directly to waits without repeating By strategy |
| One locator file per page | Easy to find and update when UI changes |
| Follow PEP 8 naming | Consistent, readable, professional |
| Detect Jenkins via env var | Same code runs locally and in CI without changes |
| Never hardcode waits | `time.sleep()` makes tests slow and brittle |

---

## 11. Python Naming Conventions (PEP 8)

| Type | Style | Example |
|------|-------|---------|
| Class | CamelCase | `LoginPage`, `BingLocators` |
| Function / Method | snake_case | `enter_user()`, `get_title()` |
| Variable | snake_case | `search_term`, `logged_in_url` |
| Constant | UPPER_CASE | `SUBMIT_BUTTON`, `MAX_WAIT` |
| File / Module | snake_case.py | `login_page.py`, `bing_locators.py` |
| Private member | _single_underscore | `_internal_driver` |
| Special method | __double_underscores__ | `__init__`, `__str__` |
