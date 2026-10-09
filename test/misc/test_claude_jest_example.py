from unittest.mock import call, patch

import pytest

from code.misc.claude_jest_example import ApiClient, UserService


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def user_service(api_client):
    return UserService(api_client)


@pytest.fixture
def fetch_user_spy(api_client):
    # Spy on API methods and mock their implementations
    def fake_fetch_user(user_id):
        return {'id': user_id, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}

    with patch.object(api_client, 'fetch_user', side_effect=fake_fetch_user) as spy:
        yield spy


@pytest.fixture
def save_user_spy(api_client):
    with patch.object(api_client, 'save_user', side_effect=lambda user_data: {**user_data, 'saved': True}) as spy:
        yield spy


class TestGetUserWithCache:
    def test_fetches_user_from_api_on_first_call(self, user_service, fetch_user_spy):
        user = user_service.get_user_with_cache(1)

        fetch_user_spy.assert_called_once_with(1)
        assert user == {'id': 1, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}

    def test_returns_cached_user_on_second_call_without_fetching(self, user_service, fetch_user_spy):
        # First call
        user_service.get_user_with_cache(1)

        # Second call
        user = user_service.get_user_with_cache(1)

        # API should only be called once
        assert fetch_user_spy.call_count == 1
        assert user['name'] == 'John Doe'

    def test_fetches_different_users_separately(self, user_service, fetch_user_spy):
        user_service.get_user_with_cache(1)
        user_service.get_user_with_cache(2)

        assert fetch_user_spy.call_args_list == [call(1), call(2)]

    def test_clears_cache_properly(self, user_service, fetch_user_spy):
        user_service.get_user_with_cache(1)
        user_service.clear_cache()
        user_service.get_user_with_cache(1)

        # Should fetch twice since cache was cleared
        assert fetch_user_spy.call_count == 2


class TestUpdateUserAge:
    def test_fetches_user_updates_age_and_saves(self, user_service, fetch_user_spy, save_user_spy):
        updated_user = user_service.update_user_age(1, 35)

        fetch_user_spy.assert_called_with(1)
        save_user_spy.assert_called_with({'id': 1, 'name': 'John Doe', 'age': 35, 'email': 'john@example.com'})
        assert updated_user['age'] == 35

    def test_raises_error_for_negative_age(self, user_service, fetch_user_spy, save_user_spy):
        with pytest.raises(ValueError, match='Invalid age'):
            user_service.update_user_age(1, -5)

        save_user_spy.assert_not_called()

    def test_raises_error_for_age_over_150(self, user_service, fetch_user_spy, save_user_spy):
        with pytest.raises(ValueError, match='Invalid age'):
            user_service.update_user_age(1, 200)

        save_user_spy.assert_not_called()

    def test_updates_cache_after_saving(self, user_service, fetch_user_spy, save_user_spy):
        user_service.update_user_age(1, 40)

        # Get user again - should use cached updated value
        user = user_service.get_user_with_cache(1)

        # fetch_user should only be called once (during update)
        assert fetch_user_spy.call_count == 1
        assert user['age'] == 40

    def test_uses_cached_user_if_available(self, user_service, fetch_user_spy, save_user_spy):
        # Pre-populate cache
        user_service.get_user_with_cache(1)

        # Update age
        user_service.update_user_age(1, 45)

        # Should still only fetch once (from first call)
        assert fetch_user_spy.call_count == 1
        assert save_user_spy.call_count == 1


class TestSpyWithDifferentMockReturnValues:
    def test_handles_api_errors_gracefully(self, user_service, fetch_user_spy):
        fetch_user_spy.side_effect = ConnectionError('Network error')

        with pytest.raises(ConnectionError, match='Network error'):
            user_service.get_user_with_cache(1)

    def test_can_mock_different_users_for_different_ids(self, user_service, fetch_user_spy):
        fetch_user_spy.side_effect = [
            {'id': 1, 'name': 'Alice', 'age': 25},
            {'id': 2, 'name': 'Bob', 'age': 30},
        ]

        user1 = user_service.get_user_with_cache(1)
        user2 = user_service.get_user_with_cache(2)

        assert user1['name'] == 'Alice'
        assert user2['name'] == 'Bob'
