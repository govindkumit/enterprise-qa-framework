from api.users_api import UsersAPI


def test_get_user():

    api = UsersAPI()

    response = api.get_user(1)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "email" in data