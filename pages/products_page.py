from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Product
    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    # Cart
    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def add_backpack_to_cart(self):

        print("Current URL before adding product:", self.driver.current_url)

        # Find Add to Cart button
        add_button = self.wait.until(
            EC.visibility_of_element_located(
                self.ADD_BACKPACK_BUTTON
            )
        )

        print("Backpack Add to Cart button visible")

        # Make sure button is in view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_button
        )

        print("Add to Cart button scrolled into view")

        # Wait until clickable
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BACKPACK_BUTTON
            )
        )

        print("Add to Cart button clickable")

        # Click
        add_button.click()

        print("Add to Cart clicked")

        # Verify cart badge
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "shopping_cart_badge")
                )
            )

            print("Cart badge appeared")

        except Exception:
            print("Cart badge was not detected")

    def open_cart(self):

        print("Current URL before opening cart:", self.driver.current_url)

        # ---------------------------------------------------------
        # 1. Find cart
        # ---------------------------------------------------------
        cart = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_LINK
            )
        )

        print("Cart link visible")

        # ---------------------------------------------------------
        # 2. Diagnostic information
        # ---------------------------------------------------------
        print("Cart text:", cart.text)
        print("Cart tag:", cart.tag_name)
        print("Cart enabled:", cart.is_enabled())
        print("Cart displayed:", cart.is_displayed())

        print(
            "Cart outerHTML:",
            cart.get_attribute("outerHTML")
        )

        # ---------------------------------------------------------
        # 3. Scroll into view
        # ---------------------------------------------------------
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            cart
        )

        print("Cart link scrolled into view")

        # ---------------------------------------------------------
        # 4. Wait until clickable
        # ---------------------------------------------------------
        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        )

        print("Cart link clickable")

        # ---------------------------------------------------------
        # 5. Normal Selenium click
        # ---------------------------------------------------------
        cart.click()

        print("Normal Selenium cart click executed")

        # ---------------------------------------------------------
        # 6. Check navigation
        # ---------------------------------------------------------
        try:

            self.wait.until(
                EC.url_contains("cart.html")
            )

            print("Cart navigation succeeded with normal click")
            print("Current URL after opening cart:", self.driver.current_url)

            return

        except Exception:

            print("Normal cart click did not navigate")
            print(
                "URL after normal cart click:",
                self.driver.current_url
            )

        # ---------------------------------------------------------
        # 7. Re-find cart
        # ---------------------------------------------------------
        cart = self.wait.until(
            EC.presence_of_element_located(
                self.CART_LINK
            )
        )

        print("Cart link found again")

        # ---------------------------------------------------------
        # 8. JavaScript fallback
        # ---------------------------------------------------------
        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        print("JavaScript cart click executed")

        # ---------------------------------------------------------
        # 9. Wait for cart page
        # ---------------------------------------------------------
        self.wait.until(
            EC.url_contains("cart.html")
        )

        print("Cart navigation succeeded with JavaScript click")
        print("Current URL after opening cart:", self.driver.current_url)