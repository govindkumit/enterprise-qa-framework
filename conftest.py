import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():

    options = Options()

    # ---------------------------------------------------------
    # Basic Chrome settings
    # ---------------------------------------------------------

    # Start maximized
    options.add_argument("--start-maximized")

    # Reduce automation-related browser UI interference
    options.add_argument("--disable-notifications")

    # Disable Chrome's password manager
    options.add_argument("--disable-save-password-bubble")

    # ---------------------------------------------------------
    # Disable Chrome password manager / leak detection
    # ---------------------------------------------------------

    options.add_experimental_option(
        "prefs",
        {
            # Disable password saving
            "credentials_enable_service": False,

            # Disable Chrome password manager
            "profile.password_manager_enabled": False,

            # Disable password leak/breach detection popup
            "profile.password_manager_leak_detection": False,
        }
    )

    # ---------------------------------------------------------
    # Selenium automation
    # ---------------------------------------------------------

    driver = webdriver.Chrome(options=options)

    # Explicit Selenium window size
    driver.set_window_size(1920, 1080)

    # ---------------------------------------------------------
    # Test starts here
    # ---------------------------------------------------------

    yield driver

    # ---------------------------------------------------------
    # Test finished
    # ---------------------------------------------------------

    driver.quit()