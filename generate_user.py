from app.movie.domain.entities.user import User
from app.movie.services.movie_service import create_new_movie
from app.movie.services.user_service import  create_new_user, filter_role_and_email
from app.application.validator.movie import  to_date
user_dummy = User(role="admin", fullname="Dummy",email="Dummy@mail.com", username="userdummy", password="dummy")


user_exists = filter_role_and_email(user=user_dummy, email="admin67@gmail.com", role="")
if not user_exists:
    create_new_user(
        user=user_dummy, 
        fullname="Super Admin",
        email="admin67@gmail.com",
        username="admin",
        password="admin123",
        role="admin"
    )