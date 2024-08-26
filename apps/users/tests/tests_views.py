from rest_framework import status
from rest_framework.reverse import reverse_lazy
import pytest


@pytest.mark.django_db
class TestViews:
    def test_users_list(self, client, users):
        url = reverse_lazy('users:user-list')

        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK, 'status code da nimadir error'
        response = response.json()
        assert len(response) == 10
        assert set(response[0]) == {'id', 'username', 'email'}

