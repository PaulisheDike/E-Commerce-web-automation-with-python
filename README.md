**E-Commerce Platform Automation Testing**

**Project Overview**
This project automates testing for an e-commerce platform, focusing on validating core functionalities such as user login, product listing, cart management, and checkout. It uses Selenium WebDriver with Python and Pytest as the testing framework.

**Table of Contents**

1. [x] Project Overview
2. [x] Technologies Used
3. [x] Setup and Installation
4. [x] Project Structure
5. [x] Configuration
6. [x] Running the Tests
7. [x] Test Cases
8. [x] Contributing
9. [x] License

**Technologies Used**

**Python**: Programming language

**Selenium WebDriver**: For browser automation

**Pytest**: Testing framework for unit and functional testing

**Allure (optional)**: For reporting and visualization of test results

**Setup and Installation**
**Prerequisites**

1. [ ] Python 3.x installed on your machine
3. [ ] ChromeDriver matching the version of your installed Chrome browser
5. [ ] Install a virtual environment (recommended)

**Installation Steps**

**Clone the repository**:

git clone <your-repo-url>
cd e-commerce_project
Create and activate a virtual environment:


python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

**Install the required packages:**

pip install -r requirements.txt
Download ChromeDriver and place it in the project's root directory, or update its path in the code configuration.

**Project Structure**

e-commerce_project/

├── Pages/                  # Page Object classes for different parts of the application

├── TestCases/              # Test classes containing test cases for each feature

├── Utilities/              # Helper functions and utility files

├── requirements.txt        # List of required Python packages

└── README.md               # Project documentation

**Important Files**

**Pages**: Contains LoginPage, CartPage, etc., implementing page actions using Selenium WebDriver.

**TestCases:** Each test class (e.g., test_all_functionalities.py) represents a specific feature with test methods.

**Utilities**: Common functions like configuration loading, logging, and test setup.

**Configuration**

**URL**: The application URL is set in config.py (typically located in Utilities or project root).

**Login Credentials**: Define your test credentials in the test_login_functionality.py file or in environment variables for security.

**ChromeDriver Path**: Update the path in test files if ChromeDriver is not in the project root.

**Running the Tests**
To run individual tests or all tests, use the following commands from the project root:

**Run All Tests**

pytest --maxfail=5 --disable-warnings

**Run Specific Test**

pytest TestCases/test_login_functionality.py::TestLogin::test_validate_sub_total

**Generate Allure Report (optional)**

To install Allure, visit Allure installation instructions.


pytest --alluredir=reports/allure-results

allure serve reports/allure-results

**Test Cases**

**Login Functionality**

**Test Valid Login**: Verifies successful login with valid credentials.

**Test Invalid Login**: Checks error handling for invalid credentials.

**Cart Management**
**Add to Cart**: Ensures items can be added to the cart.

**Remove from Cart**: Tests removal functionality of items in the cart.

**Checkout Process**

**Verify Subtotal**: Checks if the displayed subtotal matches the calculated value.

**Successful Checkout**: Completes checkout for valid user information.

**Contributing**

Feel free to fork this project, create a new branch, and submit a pull request for improvements or additional features. Ensure tests are included for any new features added.


**License**

This project is licensed under the MIT License.

