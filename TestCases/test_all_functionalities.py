import pytest
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import plotly.graph_objects as go

from Pages.cartPage import CartPage
from Pages.inventoryPage import Products
from Pages.loginPage import LoginPage
from configTest import *


@pytest.mark.usefixtures("browser_setup")
class TestLogin(unittest.TestCase):

    def setUp(self):
        # Set up the browser and page instances for each test case
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)
        self.inventory_page = Products(self.driver)
        self.cart_page = CartPage(self.driver)

    def tearDown(self):
        # Log out if logged in to ensure a clean state for the next test
        if hasattr(self, 'login_page') and self.login_page.is_logged_in():
            self.inventory_page.logout()
        self.driver.delete_all_cookies()  # Clear cookies for a fresh session
        self.driver.refresh()  # Refresh to ensure a clean state

    def checkout_user_information(self):
        self.cart_page.enter_cart_details(first_name, last_name, postal_code)

    def test_valid_login(self):
        self.login_page.login(validUsername, validPassword)
        actual_title = self.inventory_page.get_page_title()
        expect_title = self.inventory_page.Inventory_title
        assert actual_title == expect_title

    def test_invalid_login(self):
        self.login_page.login(invalidUsername, invalidPassword)
        assert self.login_page.is_visible(self.login_page.login_err_loc)

    def test_logout(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.logout()
        assert self.login_page.is_visible(self.login_page.login_btn_loc)

    def test_add_to_cart(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.click_add_to_cart_button()
        assert self.inventory_page.is_visible(self.inventory_page.cart_badge_loc)

    def test_remove_from_cart(self):
        self.login_page.login(validUsername, validPassword)

        # Ensure "Add to Cart" button is visible and clickable
        try:
            add_to_cart_button = self.inventory_page.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            # Scroll into view and click the button
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Add to Cart button was not clickable within the time limit.")

        # Now proceed to remove from cart and check if removal was successful
        self.inventory_page.remove_from_cart()
        assert not self.inventory_page.is_visible(self.inventory_page.cart_badge_loc)

    def test_validate_sub_total(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.click_add_to_cart_button()
        self.inventory_page.open_cart()
        self.cart_page.click_checkout_button()
        self.checkout_user_information()
        self.assertAlmostEqual(self.cart_page.calculate_sub_total(), self.cart_page.get_actual_sub_total(), places=2)

    def test_validate_tax(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.click_add_to_cart_button()
        self.inventory_page.open_cart()
        self.cart_page.click_checkout_button()
        self.checkout_user_information()

        expected_tax = self.cart_page.calculate_tax()
        actual_tax = self.cart_page.get_actual_tax()
        self.assertAlmostEqual(actual_tax, expected_tax, places=2)

    def test_validate_grand_total(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.click_add_to_cart_button()
        self.inventory_page.open_cart()
        self.cart_page.click_checkout_button()
        self.checkout_user_information()

        expected_grand_total = self.cart_page.calculate_grand_total()
        actual_grand_total = self.cart_page.get_actual_grand_total()
        self.assertAlmostEqual(actual_grand_total, expected_grand_total, places=2)

    def test_validate_successful_checkout(self):
        self.login_page.login(validUsername, validPassword)
        self.inventory_page.click_add_to_cart_button()
        self.inventory_page.open_cart()
        self.cart_page.click_checkout_button()
        self.checkout_user_information()
        self.cart_page.click_finish_button()
        actual_checkout_msg = "Thank you for your order!"
        self.assertEqual(self.cart_page.is_checkout_successful(), actual_checkout_msg)

