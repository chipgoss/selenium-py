# selenium-py
Simple Python + Selenium automation demo using Page Object Model (POM) pattern.

### Purpose
This project is a minimal, clean example of Selenium test automation in Python.  
It demonstrates:
- Page Object Model (POM) for maintainable code
- Separate locators file for easy UI changes
- Basic console reporting (PASS/FAIL with timestamps and details)
- Automatic screenshots on failure
- Allure reporting integration for rich test results
- No heavy dependencies or reporting frameworks (KISS principle)

Goal: Show recruiters I can write structured, readable Selenium tests in Python.

### Project Structure
```
selenium-py/
├── tests/
│   ├── __init__.py
│   ├── test_01_DuckDuckGo.py   # Search DuckDuckGo & assert title
│   ├── test_02_Bing.py         # Search Bing & assert title
│   └── test_03_Login.py        # Login to the-internet.herokuapp.com & assert URL
├── pages/
│   ├── duckduckgo_page.py
│   ├── bing_page.py
│   └── login_page.py
├── locators/
│   ├── duckduckgo_locators.py
│   ├── bing_locators.py
│   └── login_locators.py
└── reports/
    └── screenshots/
```

### Tests
| # | Test | Site | Assertion |
|---|------|------|-----------|
| 01 | DuckDuckGo Search | duckduckgo.com | Search term appears in page title |
| 02 | Bing Search | bing.com | Search term appears in page title |
| 03 | Login | the-internet.herokuapp.com | URL contains `/secure` after login |

### How to Run
1. Install dependencies:
```bash
pip install selenium webdriver-manager allure-pytest
```
2. Run all tests:
```bash
pytest tests/
```
3. Run with Allure reporting:
```bash
pytest tests/ --alluredir=allure-results
```
4. Run a specific test:
```bash
pytest tests/test_03_Login.py::test_login
```

### Jenkins CI/CD Setup
This project is configured to run automatically on a Windows-based Jenkins server using a Declarative Pipeline.

**Prerequisites**
- Python 3.14+: Installed at `C:\Users\cagoss\AppData\Local\Programs\Python\Python314`
- Chrome Browser: Installed on the Jenkins agent (runs in `--headless` mode)
- Jenkins Plugins: JUnit Plugin, Pipeline, Allure

**Local Execution**
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `pytest tests/ --junitxml=results.xml --alluredir=allure-results`

**Jenkins Configuration Note**
The Jenkinsfile uses absolute paths for the Python executable to ensure the Jenkins Service can locate the environment. If your Python installation path differs, update the Install Dependencies stage in the Jenkinsfile.

### Python Naming Conventions (PEP 8 Quick Guide)

| Type | Style | Example |
|------|-------|---------|
| Class | CamelCase | `DuckDuckGoPage` |
| Function / Variable | snake_case | `search_term`, `get_page_title()` |
| Constant | UPPER_CASE | `MAX_WAIT_TIME = 10` |
| File / Module | snake_case.py | `duckduckgo_page.py` |
| Private member | _single_underscore | `_internal_driver` |
| Special method | double_underscores | `__init__`, `__str__` |

Feel free to clone/fork and add more tests. Feedback welcome!
