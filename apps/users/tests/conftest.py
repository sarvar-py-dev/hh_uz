import pytest

from users.tests.factories import UserFactory


@pytest.fixture
def users():
    return UserFactory.create_batch(10)
