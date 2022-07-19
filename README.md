# pytest_allure_test_project

## About The Project
Web UI automation tests for site https://www.saucedemo.com with Allure reporting support.

### Built With
- [Selenium](https://pypi.org/project/selenium)
- [Pytest](https://pypi.org/project/pytest/)
- [Allure Pytest Plugin](https://pypi.org/project/allure-pytest/)

## Getting started

### Prerequisites
- Python 3.7+
- [Chromedriver](https://chromedriver.chromium.org/) - if you want to run tests with Chrome.
- [Geckodriver](https://github.com/mozilla/geckodriver) - if you want to run tests with  Firefox.
- [Allure](https://docs.qameta.io/allure/#_installing_a_commandline) - if you want to generate reports locally.

### Installation
1. Clone the repo - `git clone https://github.com/nzhernovkov/pytest_allure_test_project.git`
2. Install packages - `pip install -r requirements.txt`

## Usage
1. Run tests - `pytest -n auto --alluredir=./tmp/my_allure_results --browser_name=chrome`
2. Generate Allure report (if you have installed Allure) - `allure serve ./tmp/my_allure_results`