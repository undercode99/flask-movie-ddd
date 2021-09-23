from werkzeug.security import generate_password_hash, check_password_hash
from app.infrastructure.persistence.sqlalchemy.repositories.user_repository import UserSqlAlchemyRepository
from app.movie.domain.entities.user import User
from app.movie.domain.value_object.roles import Roles
from datetime import date
from app.movie.services.auth_services import check_authorization


"""
Select all user
"""
def select_all_user(user: User):
    check_authorization(user, "add_user")
    return UserSqlAlchemyRepository.all()


"""
Create new user 
"""
def create_new_user(user: User, fullname, username, email, role, password):
    """ Auth services """
    check_authorization(user, "add_user")
    
    """ User username and email must unique """
    user_must_unique(username=username, email=email)
    users = UserSqlAlchemyRepository.add(
        User(
            fullname=fullname, 
            username=username,
            email=email,
            role=role,
            password=generate_password_hash(password),
        )
    )
    return users


"""
Delete user by id
"""
def delete_data_user(user: User, user_id):
    """ Auth services """
    check_authorization(user, "delete_user")

    if user.id == user_id:
        raise ValueError("You can't delete your own account")

    return UserSqlAlchemyRepository.deleteById(user_id)

"""
Get user by id
"""
def first_data_user(user: User,  user_id):
    """ Auth services """
    check_authorization(user, "read_user")
    return UserSqlAlchemyRepository.get(user_id)

"""
Update data user 
"""
def update_data_user(user: User, id, fullname, username, email, role, password):
    """ Auth services """
    check_authorization(user, "edit_user")

    user_must_unique(id=id, username=username, email=email)
    user = User(
        id=id,
        fullname=fullname, 
        username=username,
        email=email,
        role=role,
        password=generate_password_hash(password) if password != "" else "",
    )
    return UserSqlAlchemyRepository.update(user)


"""
Check unique data user email & usernama
"""
def user_must_unique(username, email, id = None):
    email_unique = UserSqlAlchemyRepository.checkEmailMustUnique(id = id, email=email)
    if not email_unique: raise ValueError("Email is already in use by another user")

    username_unique = UserSqlAlchemyRepository.checkUsernameMustUnique(id = id, username=username)
    if not username_unique: raise ValueError("Username is already in use by another user")
    


def filter_role_and_email(user: User, role, email) -> list:
    """ Auth services """
    check_authorization(user, "read_user")
    return UserSqlAlchemyRepository.filterByRoleAndLikeEmail(role=role, email=email)