from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Test data
BaseUrl = "https://www.saucedemo.com/"
validUsername = "standard_user"
validPassword = "secret_sauce"
invalidUsername = "standard"
invalidPassword = "secret_"

first_name = "Goddey"
last_name = "Paul"
postal_code = "10001"


@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    print("Initializing Chrome Driver...")
    chrome_options = Options()
    chrome_options.page_load_strategy = 'normal' # Options: 'normal', 'eager', 'none'
    request.cls.driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver.maximize_window()
    # Set the page load timeout (in seconds)
    request.cls.driver.set_page_load_timeout(30)
    yield
    print("Quitting Chrome Driver...")
    request.cls.driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create a reports directory if it doesn't exist
    report_dir = Path("Reports")
    report_dir.mkdir(exist_ok=True)

    # Generate a unique report file name
    report_file = report_dir / f"Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    # Set the path for the HTML report
    config.option.htmlpath = str(report_file)
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "E-Commerce Test Report for Gridiron"