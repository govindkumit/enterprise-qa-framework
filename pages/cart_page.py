from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Checkout button
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):

        print("Current URL before checkout:", self.driver.current_url)

        # ---------------------------------------------------------
        # 1. Find checkout button
        # ---------------------------------------------------------
        checkout_button = self.wait.until(
            EC.visibility_of_element_located(self.CHECKOUT_BUTTON)
        )

        print("Checkout button visible")

        # ---------------------------------------------------------
        # 2. Print diagnostic information
        # ---------------------------------------------------------
        print("Checkout button text:", checkout_button.text)
        print("Checkout button tag:", checkout_button.tag_name)
        print("Checkout button enabled:", checkout_button.is_enabled())
        print("Checkout button displayed:", checkout_button.is_displayed())

        print(
            "Checkout button outerHTML:",
            checkout_button.get_attribute("outerHTML")
        )

        # ---------------------------------------------------------
        # 3. Scroll button into view
        # ---------------------------------------------------------
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            checkout_button
        )

        print("Checkout button scrolled into view")

        # ---------------------------------------------------------
        # 4. Wait until Selenium considers it clickable
        # ---------------------------------------------------------
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        print("Checkout button clickable")

        # ---------------------------------------------------------
        # 5. Try normal Selenium click
        # ---------------------------------------------------------
        checkout_button.click()

        print("Normal Selenium click executed")

        # ---------------------------------------------------------
        # 6. Give browser a moment to process JavaScript
        # ---------------------------------------------------------
        try:
            self.wait.until(
                EC.url_contains("checkout-step-one.html")
            )

            print("Checkout navigation succeeded with normal click")
            print("Current URL after checkout:", self.driver.current_url)
            return

        except Exception:
            print("Normal click did not navigate to checkout")
            print("URL after normal click:", self.driver.current_url)

        # ---------------------------------------------------------
        # 7. Re-find the button
        # ---------------------------------------------------------
        checkout_button = self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        )

        print("Checkout button found again")

        # ---------------------------------------------------------
        # 8. JavaScript click fallback
        # ---------------------------------------------------------
        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        print("JavaScript click executed")

        # ---------------------------------------------------------
        # 9. Wait for checkout page
        # ---------------------------------------------------------
        self.wait.until(
            EC.url_contains("checkout-step-one.html")
        )

        print("Checkout navigation succeeded with JavaScript click")
        print("Current URL after checkout:", self.driver.current_url)