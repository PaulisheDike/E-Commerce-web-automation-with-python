from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.utilities import Utilities


class Products(Utilities):

    #locators
    product_page_title_loc = (By.XPATH, "//span[@class='title']")
    Inventory_title = "Products"
    hamburger_menu_loc = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_loc = (By.XPATH, "//a[@id='logout_sidebar_link']")
    add_to_cart_btn_loc = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    cart_badge_loc = (By.XPATH, "//span[@class='shopping_cart_badge']")
    remove_btn_loc = (By.XPATH, "//button[contains(text(), 'Remove')]")
    shopping_cart_loc = (By.XPATH, "//a[@class='shopping_cart_link']")

    # create a constructor
    def __init__(self, driver):
        # Call constructor of parent class
        super().__init__(driver)
        # self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    # Returns the page header - Products
    def get_page_title(self):
        return self.get_text(self.product_page_title_loc)

    # This logs out the user
    def logout(self):
        self.click_something(self.hamburger_menu_loc)
        self.click_something(self.logout_loc)

    # This will add the selected item to the chat
    def click_add_to_cart_button(self):
        try:
            # Ensure page is loaded and element is ready to be clicked
            self.driver.refresh()
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            # Scroll into view and click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
            add_to_cart_button.click()
        except TimeoutException:
            raise Exception("Add to Cart button was not clickable within the time limit.")
    # Verify product was successfully added to cart
    def is_product_added_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_badge_loc))
        return self.driver.find_element(self.cart_badge_loc).is_displayed()

    # Open cart to view items added to cart
    def open_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.shopping_cart_loc))
        self.click_something(self.shopping_cart_loc)

    # Remove products added to cart
    def remove_from_cart(self):

        self.open_cart()
        self.wait.until(EC.visibility_of_element_located(self.remove_btn_loc))
        remove_buttons = self.driver.find_elements(*self.remove_btn_loc)
        for button in remove_buttons:
            button.click()

    # Verify that product is removed from cart
    def is_product_removed_from_cart(self):
        try:
            element = self.driver.find_element(By.XPATH, self.cart_badge_loc)
            return element.is_displayed()
        except NoSuchElementException:
            return False



