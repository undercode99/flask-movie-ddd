import pytest
import os
from app.movie.services.user_service import select_all_user, create_new_user, first_data_user, update_data_user, user_must_unique
from app.movie.domain.entities.user import User
from app.movie.domain.value_object.roles import Roles

def user_staff():
    return User(email="staff@gmail.com", username="staff", fullname="User Staff", password="Uu676611s", role=Roles.Staff)

def user_admin():
    return User(email="admin@gmail.com", username="admin", fullname="User Admin", password="Uu6766s11", role=Roles.Admin)


def assert_obj_user_model(obj1, obj2):
    assert obj1.id == obj2.id
    assert obj1.email == obj2.email
    assert obj1.username == obj2.username
    assert obj1.fullname == obj2.fullname
    assert obj1.password == obj2.password
    assert obj1.role == obj2.role


def test_select_all_user():
    create_new_user(user_admin(), email="nim4n136@gmail.com", username="nim4n136", fullname="Mohamad Usman", password="Uu6766s", role="admin")
    create_new_user(user_admin(), email="usman136@gmail.com", username="mohusman", fullname="Jhone", password="121211", role="staff")
    users = select_all_user(user_admin())
    assert len(users) >= 2


def test_first_data_user():
    user = create_new_user(user_admin(), email="dragon@gmail.com", username="dragon666", fullname="Mr Dragon", password="xxxx", role="staff")
    first = first_data_user(user_admin(), user.id)
    assert_obj_user_model(user, first)

def test_update_data_user():
    user = create_new_user(user=user_admin(), email="update@gmail.com", username="updasd22", fullname="Mr xxx", password="xxxx", role="staff")
    update_data_user(user=user_admin(), id=user.id, email="newupdate@gmail.com", username="xxxx", fullname="mantaps", password="", role="")
    first = first_data_user(user_admin(), user.id)
    
    # Check has edited
    assert first.email != user.email
    assert first.username != user.username
    assert first.fullname != user.fullname

    # Check not edited
    assert first.password == user.password
    assert first.role == user.role


def test_user_must_unique():
    # error
    with pytest.raises(ValueError):
        user_must_unique(email="nim4n136@gmail.com", username="nim4n136")

    # valid
    user_must_unique(email="randiom@gmail.com", username="dasdkjasdajda89da")
