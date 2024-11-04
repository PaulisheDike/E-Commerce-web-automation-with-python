from Base.utilities import Utilities
from selenium.webdriver.common.by import By

#create a login page class to inherit the utilities clas
class LoginPage(Utilities):

    #locators
    username_loc = (By.XPATH, "//input[@id='user-name']")
    password_loc = (By.XPATH, "//input[@id='password']")
    login_btn_loc = (By.XPATH, "//input[@id='login-button']")
    login_err_loc = (By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
    logout_loc = (By.XPATH, "//a[@id='logout_sidebar_link']")



   #create a constructor
    def __init__(self, driver):

        #Call constructor of parent class
        super().__init__(driver)

    #create login function
    def login(self, username, password):
        self.type_something(self.username_loc, username)
        self.type_something(self.password_loc, password)
        self.click_something(self.login_btn_loc)

    # Check for login
    def is_logged_in(self):
        # Check if user is logged in
        self.is_visible(self.logout_loc)

