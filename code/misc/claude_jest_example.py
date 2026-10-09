import json
import urllib.request


class ApiClient:
    def fetch_user(self, user_id):
        # Simulates API call
        with urllib.request.urlopen(f'https://api.example.com/users/{user_id}') as response:
            return json.load(response)

    def save_user(self, user_data):
        # Simulates saving to API
        request = urllib.request.Request(
            'https://api.example.com/users',
            data=json.dumps(user_data).encode(),
            method='POST',
        )
        with urllib.request.urlopen(request) as response:
            return json.load(response)


class UserService:
    def __init__(self, api_client):
        self.api_client = api_client
        self.cache = {}

    def get_user_with_cache(self, user_id):
        # Check cache first
        if user_id in self.cache:
            return self.cache[user_id]

        # Fetch from API if not cached
        user = self.api_client.fetch_user(user_id)
        self.cache[user_id] = user
        return user

    def update_user_age(self, user_id, new_age):
        user = self.get_user_with_cache(user_id)

        if new_age < 0 or new_age > 150:
            raise ValueError('Invalid age')

        updated_user = {**user, 'age': new_age}
        self.api_client.save_user(updated_user)

        # Update cache
        self.cache[user_id] = updated_user
        return updated_user

    def clear_cache(self):
        self.cache.clear()
