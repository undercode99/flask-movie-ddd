import pytest
import os
from .test_user_service import user_admin, user_staff
from app.movie.services.auth_services import check_user_password, check_authorization
from app.movie.services.user_service import create_new_user


def test_check_user_password():
    create_new_user(user_admin(),email="sampleemail11@gmail.com", username="sampleemail11", fullname="Mohamad Usman", password="doooiiid", role="staff")
    assert check_user_password(password="doooiiid", username="sampleemail11") != None


def test_check_authorization():
    assert check_authorization(user_admin(), "add_movie") == True
    assert check_authorization(user_admin(), "edit_movie") == True
    assert check_authorization(user_admin(), "delete_movie") == True
    assert check_authorization(user_admin(), "add_user") == True
    assert check_authorization(user_admin(), "edit_user") == True
    assert check_authorization(user_admin(), "delete_user") == True
    assert check_authorization(user_staff(), "edit_movie") == True

    with pytest.raises(ValueError):
        check_authorization(user_staff(), "add_movie") == False
        check_authorization(user_staff(), "delete_movie") == False
        check_authorization(user_staff(), "add_user") == False
        check_authorization(user_staff(), "edit_user") == False
        check_authorization(user_staff(), "delete_user") == False

    
