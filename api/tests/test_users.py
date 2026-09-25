import requests
import pytest
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression

def test_get_user():

    url = "https://reqres.in/api/users/2"

    response = requests.get(url)

    print("Status code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200