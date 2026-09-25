from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    # =========================================================
    # Checkout Step One
    # =========================================================

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    # =========================================================
    # Checkout Step Two
    # =========================================================

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    # =========================================================
    # Checkout Complete
    # =========================================================

    COMPLETE_HEADER = (
        By.CLASS_NAME,
        "complete-header"
    )

    # =========================================================
    # Enter customer details
    # =========================================================

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        first_name_field.clear()

        first_name_field.send_keys(
            first_name
        )

        last_name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        last_name_field.clear()

        last_name_field.send_keys(
            last_name
        )

        postal_code_field = self.wait.until(
            EC.visibility_of_element_located(
                self.POSTAL_CODE
            )
        )

        postal_code_field.clear()

        postal_code_field.send_keys(
            postal_code
        )

        print("Customer details entered")

    # =========================================================
    # Continue from Step One to Step Two
    # =========================================================

    def continue_checkout(self):

        print(
            "Current URL before Continue:",
            self.driver.current_url
        )

        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        print("Continue button found")

        # Make sure button is visible in browser
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            continue_button
        )

        print(
            "Continue button scrolled into view"
        )

        # Normal Selenium click
        continue_button.click()

        print(
            "Continue button clicked"
        )

        # Wait for checkout step two
        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

        print(
            "Successfully navigated to:",
            self.driver.current_url
        )

    # =========================================================
    # Complete order
    # =========================================================

    def complete_order(self):

        print(
            "Current URL before Finish:",
            self.driver.current_url
        )

        print(
            "Page title:",
            self.driver.title
        )

        # Make sure we are on checkout step two
        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

        print(
            "Checkout step two loaded"
        )

        finish_button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        print(
            "Finish button found"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            finish_button
        )

        finish_button.click()

        print(
            "Finish button clicked"
        )

        # Wait for order completion
        self.wait.until(
            EC.url_contains(
                "checkout-complete.html"
            )
        )

        print(
            "Order completed"
        )

        print(
            "Final URL:",
            self.driver.current_url
        )

    # =========================================================
    # Get confirmation message
    # =========================================================

    def get_confirmation_message(self):

        confirmation = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        )

        return confirmation.text