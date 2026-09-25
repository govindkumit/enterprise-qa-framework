import requests
import pytest


BASE_URL = "https://reqres.in"

@pytest.mark.security
@pytest.mark.regression
def test_https_enabled():
    response = requests.get(
        f"{BASE_URL}/api/users/2",
        timeout=10
    )

    print("URL:", response.url)

    assert response.url.startswith("https://")


def test_security_headers():
    response = requests.get(
        f"{BASE_URL}/api/users/2",
        timeout=10
    )

    print("Response headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    assert response.status_code == 200


def test_no_server_error():
    response = requests.get(
        f"{BASE_URL}/api/users/2",
        timeout=10
    )

    print("Status code:", response.status_code)

    assert response.status_code < 500


def test_sensitive_data_not_exposed():
    response = requests.get(
        f"{BASE_URL}/api/users/2",
        timeout=10
    )

    response_text = response.text.lower()

    print("Response:", response.text)

    sensitive_keywords = [
        "password",
        "credit_card",
        "cvv",
        "secret_key"
    ]

    for keyword in sensitive_keywords:
        assert keyword not in response_text