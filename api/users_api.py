import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


class UsersAPI:

    def get_user(self, user_id):
        return requests.get(
            f"{BASE_URL}/users/{user_id}"
        )

    def create_user(self, payload):
        return requests.post(
            f"{BASE_URL}/users",
            json=payload
        )

    def update_user(self, user_id, payload):
        return requests.put(
            f"{BASE_URL}/users/{user_id}",
            json=payload
        )

    def delete_user(self, user_id):
        return requests.delete(
            f"{BASE_URL}/users/{user_id}"
        )