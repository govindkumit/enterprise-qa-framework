from selenium.webdriver.common.by import By


class GooglePage:

    def __init__(self, driver):
        self.driver = driver

        self.search_box = (By.NAME, "q")

    def open(self, url):
        self.driver.get(url)

    def search(self, text):
        self.driver.find_element(*self.search_box).send_keys(text)

    def get_title(self):
        return self.driver.title