from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from Base.utilities import Utilities


class CartPage(Utilities):

    #Locators
    cart_btn = (By.XPATH,"//a[@class='shopping_cart_link']")
    checkout_btn_loc = (By.XPATH,"//button[@id='checkout']")
    continue_shopping_btn = (By.XPATH,"//button[@id='continue-shopping']")
    first_name_loc = (By.XPATH,"//input[@id='first-name']")
    last_name_loc = (By.XPATH,"//input[@id='last-name']")
    postal_code_loc = (By.XPATH,"//input[@id='postal-code']")
    continue_btn_loc = (By.XPATH,"//input[@id='continue']")
    item_price_loc = (By.XPATH,"//div[@class='inventory_item_price'][contains(text(),'$')]")
    sub_total_loc = (By.XPATH,"//div[@class='summary_subtotal_label']")
    tax_loc = (By.XPATH,"//div[@class='summary_tax_label']")
    grand_total_loc = (By.XPATH,"//div[@class='summary_total_label']")
    finish_btn_loc = (By.XPATH,"//button[@id='finish']")
    order_complete_loc = (By.XPATH,"//h2[@class='complete-header']")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Set wait time

    # Checkout all items in the cart
    def click_checkout_button(self):
        self.wait.until(EC.visibility_of_element_located(self.checkout_btn_loc))
        self.click_something(self.checkout_btn_loc)

    # Enter customer details for the order
    def enter_cart_details(self,firstname,lastname,postalcode):
        self.type_something(self.first_name_loc,firstname)
        self.type_something(self.last_name_loc,lastname)
        self.type_something(self.postal_code_loc,postalcode)
        self.click_something(self.continue_btn_loc)

    def calculate_sub_total(self):
        self.wait.until(EC.visibility_of_element_located(self.item_price_loc))
        cart_items = self.driver.find_elements(*self.item_price_loc)
        total_price = sum(float(price.text.replace("$", "").replace(",", "")) for price in cart_items)
        print(total_price)
        return total_price

    def get_actual_sub_total(self):
        # Wait for the subtotal element to be visible
        self.wait.until(EC.visibility_of_element_located(self.sub_total_loc))
        actual_sub_total_element = self.driver.find_element(*self.sub_total_loc)

        # Extract the numeric part of the subtotal
        actual_sub_total_text = actual_sub_total_element.text.replace("Item total: ", "").replace("$", "").replace(",",
                                                                                                                   "")
        try:
            sub_total_price = float(actual_sub_total_text)
        except ValueError as e:
            print(f"Error converting subtotal text to float: {e}")
            raise

        return sub_total_price

    def calculate_tax(self):
        expected_tax = self.calculate_sub_total() * 0.08
        print(expected_tax)
        return expected_tax

    def get_actual_tax(self):
        # Wait until the tax element is visible
        self.wait.until(EC.visibility_of_element_located(self.tax_loc))
        actual_tax_element = self.driver.find_element(*self.tax_loc)

        # Extract the numeric part of the tax amount
        actual_tax_text = actual_tax_element.text.replace("Tax: ", "").replace("$", "").replace(",", "")
        try:
            actual_tax = float(actual_tax_text)
        except ValueError as e:
            print(f"Error converting tax text to float: {e}")
            raise

        return actual_tax

    def calculate_grand_total(self):
        return self.get_actual_sub_total() + self.calculate_tax()

    def get_actual_grand_total(self):
        self.wait.until(EC.visibility_of_element_located(self.grand_total_loc))
        actual_grand_total = self.driver.find_element(*self.grand_total_loc)

        # Remove any non-numeric text before converting to float
        actual_grand_total_text = actual_grand_total.text.replace("Total: ", "").replace("$", "").replace(",", "")
        try:
            return float(actual_grand_total_text)
        except ValueError:
            print(f"Error converting grand total text to float: {actual_grand_total_text}")
            raise

    def click_finish_button(self):
        self.wait.until(EC.visibility_of_element_located(self.finish_btn_loc)).click()

    def is_checkout_successful(self):
        try:
            # Increase the timeout duration
            self.wait.until(EC.visibility_of_element_located(self.order_complete_loc))
            order_complete_element = self.driver.find_element(*self.order_complete_loc)

            # Return the text of the confirmation message
            return order_complete_element.text
        except TimeoutException:
            print("Order completion message was not found within the timeout period.")
            print("Page source at failure:\n", self.driver.page_source)
            raise

