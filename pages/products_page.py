from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    CART = (By.ID, "shopping_cart_container")
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK)
        )

        button.click()

    def open_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART)
        )

        cart.click()

        self.wait.until(
            EC.url_contains("/cart.html")
        )