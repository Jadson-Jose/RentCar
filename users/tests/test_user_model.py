import pytest
from users.models import User

@pytest.mark.django_db
def test_creation_user():
    user = User.objects.create(
        name = "Jadson",
        email = "jadson@email.com",
        password = "password123",
        types = "client"
    )
    assert user.name == "Jadson"
    assert user.types == "client"