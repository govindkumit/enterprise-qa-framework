from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

        self.backpack = (
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        self.cart = (
            By.CLASS_NAME,
            "shopping_cart_link"
        )

    def add_backpack_to_cart(self):

        print("Current URL:", self.driver.current_url)
        print("Page title:", self.driver.title)

        print(
            "Backpack elements found:",
            len(
                self.driver.find_elements(
                    By.ID,
                    "add-to-cart-sauce-labs-backpack"
                )
            )
        )

        buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            "button"
        )

        print("Add buttons found:", len(buttons))

        for button in buttons:
            print(
                "BUTTON:",
                button.text,
                "| ID:",
                button.get_attribute("id")
            )

        self.driver.find_element(
            *self.backpack
        ).click()

    def open_cart(self):
        self.driver.find_element(
            *self.cart
        ).click()