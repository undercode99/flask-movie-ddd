from app.infrastructure.persistence.sqlalchemy.repositories.user_repository import UserSqlAlchemyRepository
from werkzeug.security import check_password_hash
from app.movie.domain.value_object.roles import ServicesRole
from app.movie.domain.entities.user import User

"""
Check password users
"""
def check_user_password(password, username = None, email = None):
    if username:
        user = UserSqlAlchemyRepository.filterBy({"username": username})
    elif email:
        user = UserSqlAlchemyRepository.filterBy({"email": email})
    else:
        raise ValueError("Wrong credentials, please fill username or email...")

    if not user:
        raise ValueError("Wrong credentials")

    if not check_password_hash(user.password, password):
        raise ValueError("Wrong credentials")
    return user


def check_user_exists(id):
  return UserSqlAlchemyRepository.get(id)


""" Check authorize user role """
def check_authorization(user: User, name_service):
    roles_services = ServicesRole.roles(user.role.value)
    if not roles_services:
        raise ValueError("Not have authorize for this services")

    if name_service not in roles_services:
        raise ValueError("Not have authorize for this services")
    return True
