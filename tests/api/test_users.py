import pytest
from models.user import User
from test_data.user_data import CREATE_USER_DATA


@pytest.mark.smoke
@pytest.mark.readonly
def test_get_user(users_api):

    response = users_api.get_user(1)

    assert response.status == 200

    data = response.json()
    user = User.from_json(data)

    assert user.id == 1
    assert user.name == "Leanne Graham"

@pytest.mark.regression
def test_create_user(users_api):

    response = users_api.create_user(CREATE_USER_DATA)

    assert response.status == 201

    data = response.json()

    assert data["name"] == "John Doe"
    assert data["username"] == "johndoe"
    assert data["email"] == "john@example.com"


@pytest.mark.regression
def test_update_user(users_api):

    updated_data = {
        "id": 1,
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com"
    }

    response = users_api.update_user(1, updated_data)

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Updated User"
    assert data["username"] == "updateduser"
    assert data["email"] == "updated@example.com"


@pytest.mark.regression
def test_delete_user(users_api):

    response = users_api.delete_user(1)

    assert response.status == 200


@pytest.mark.smoke
@pytest.mark.readonly
def test_api_health(users_api):

    response = users_api.health_check()

    assert response.status == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0



@pytest.mark.readonly
def test_find_user_without_index(users_api):

    response = users_api.get_users()

    assert response.status == 200

    users = [
        User.from_json(user_data)
        for user_data in response.json()
    ]

    user = next(
        (u for u in users if u.name == "Leanne Graham"),
        None
    )

    assert user is not None
    assert user.username == "Bret"
    assert user.email == "Sincere@april.biz"