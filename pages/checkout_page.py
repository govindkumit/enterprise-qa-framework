from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Checkout Step One
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Checkout Step Two
    FINISH_BUTTON = (By.ID, "finish")

    # Checkout Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_customer_details(self, first_name, last_name, postal_code):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self):

        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        continue_button.click()

    def complete_order(self):

        print("Current URL before Finish:", self.driver.current_url)
        print("Page title:", self.driver.title)

        # Wait for checkout step two
        self.wait.until(
            EC.url_contains("checkout-step-two.html")
        )

        print("Checkout step two loaded")

        # Wait for Finish button
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        print("Finish button found")

        finish_button.click()

        print("Finish button clicked")

        # Wait for order completion
        self.wait.until(
            EC.url_contains("checkout-complete.html")
        )

        print("Order completed")
        print("Final URL:", self.driver.current_url)

        # Wait for confirmation message
        confirmation = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )

        print("Confirmation message:", confirmation.text)

        assert "Thank you for your order" in confirmation.text

    def get_confirmation_message(self):

        confirmation = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )

        return confirmation.text