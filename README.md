README.md

```markdown
# selenium-py

Simple Python + Selenium automation demo using Page Object Model (POM) pattern.

### Purpose
This project is a minimal, clean example of Selenium test automation in Python.  
It demonstrates:
- Page Object Model (POM) for maintainable code
- Separate locators file for easy UI changes
- Basic console reporting (PASS/FAIL with timestamps and details)
- Automatic screenshots on failure
- No heavy dependencies or reporting frameworks (KISS principle)

Goal: Show recruiters I can write structured, readable Selenium tests in Python.

### Project Structure
```
selenium-py/
├── tests/
│   ├── __init__.py
│   └── test_duckduckgo.py     # Example test: search DuckDuckGo & assert title
├── pages/
│   └── duckduckgo_page.py     # Page object with actions
├── locators/
│   └── duckduckgo_locators.py # All CSS selectors in one place
└── reports/
    └── screenshots/           # Failure screenshots saved here
```

### How to Run
1. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```

2. Run the test:
   ```bash
   python tests/test_duckduckgo.py
   ```

- Browser opens automatically
- Searches DuckDuckGo for "Python Selenium automation"
- Asserts search term appears in page title
- Prints PASS/FAIL in console
- Takes screenshot if test fails (saved in `reports/screenshots/`)

### Why This Project?
- Clean, real-world POM structure
- Simple failure reporting + screenshots
- Easy to extend (add more tests/pages/locators)
- No complex setup — runs with basic pip installs

### Python Naming Conventions (PEP 8 Quick Guide)
This project follows standard Python naming conventions for readability and professionalism:

| Type                | Style                  | Example                              | Notes |
|---------------------|------------------------|--------------------------------------|-------|
| Class               | CamelCase              | DuckDuckGoPage                       | Capital words, no underscores |
| Function / Variable | snake_case             | search_term, get_page_title()        | Lowercase + underscores |
| Constant            | UPPER_CASE             | MAX_WAIT_TIME = 10                   | All caps + underscores |
| File / Module       | snake_case.py          | duckduckgo_page.py, test_search.py   | Lowercase + underscores |
| Private member      | _single_underscore     | _internal_driver                     | "Private" by convention |
| Special method      | __double_underscores__ | __init__, __str__                    | Dunder methods only |

Quick rules:
- No camelCase except classes
- No spaces or hyphens in names
- Descriptive names (avoid single letters except loop vars like `i`)
- Files/folders: always lowercase + underscores

This keeps the code clean, consistent, and easy to maintain.

## Jenkins CI/CD Setup
This project is configured to run automatically on a Windows-based Jenkins server using a Declarative Pipeline.

### Prerequisites
- **Python 3.14+**: Installed at `C:\Users\cagoss\AppData\Local\Programs\Python\Python314`
- **Chrome Browser**: Installed on the Jenkins agent (runs in `--headless` mode).
- **Jenkins Plugins**: JUnit Plugin, Pipeline.

### Local Execution
To run these tests manually on your machine:
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `pytest tests/ --junitxml=results.xml`

### Jenkins Configuration Note
The `Jenkinsfile` uses absolute paths for the Python executable to ensure the Jenkins Service (running as `LocalSystem` or `cagoss`) can locate the environment. If your Python installation path differs, update the `Install Dependencies` stage in the `Jenkinsfile`.

Feel free to clone/fork and add more search engines or assertions. Feedback welcome!
