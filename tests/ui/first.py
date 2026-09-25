from config.config import BASE_URL
from pages.google_page import GooglePage
def test_open_google(driver):
    google_page = GooglePage(driver)
    google_page.open(BASE_URL)
    assert "Google" in google_page.get_title()
  
from config.config import BASE_URL
from pages.google_page import GooglePage


def test_google_search(driver):

    google_page = GooglePage(driver)

    google_page.open(BASE_URL)

    google_page.search("Selenium Python")

    assert "Google" in google_page.get_title()