import pytest
from app.movie.services.movie_service import create_new_movie, update_data_movie, select_data_movie, delete_data_movie
from .test_user_service import user_admin, user_staff
from datetime import date

""" Test user admin add movie """
def test_create_new_movie():

    to_day = date.today()

    movie = create_new_movie(
        user=user_admin(),
        title="film title",
        description="film description",
        photo="photo.png",
        release_date=to_day,
        publish_date=to_day
    )

    assert movie.title == "film title"
    assert movie.description == "film description"
    assert movie.photo == "photo.png"
    assert movie.release_date == to_day
    assert movie.publish_date == to_day


""" Test user staff add movie """
def test_create_new_movie_by_staff():
    to_day = date.today()
    with pytest.raises(ValueError):
        create_new_movie(
            user=user_staff(),
            title="film title",
            description="film description",
            photo="photo.png",
            release_date=to_day,
            publish_date=to_day
        )


""" Test user edit movie """
def update_data_movie_by_user(user):

    to_day = date.today()

    movie = create_new_movie(
        user=user_admin(),
        title="film title",
        description="film description",
        photo="photo.png",
        release_date=to_day,
        publish_date=to_day
    )

    movie_update = update_data_movie(
        user=user,
        id=movie.id,
        title="film title updated",
        description="",
        photo="",
        release_date="",
        publish_date=""
    )

    assert movie_update.title != movie.title
    assert movie_update.description == movie.description
    assert movie_update.photo == movie.photo
    assert movie_update.release_date == movie.release_date
    assert movie_update.publish_date == movie.publish_date


""" Test user admin edit movie """
def test_update_data_movie_by_admin():
    update_data_movie_by_user(user_admin())


""" Test user staff edit movie """
def test_update_data_movie_by_staff():
    update_data_movie_by_user(user_staff())

""" Filter helper """
def filtered_movie(must_result, results):
    movie_select = None
    for i in results:
        if i.id == must_result.id:
            movie_select = i
    return movie_select


""" Test user select movie """
def select_data_movie_by_users(user):

    movie = create_new_movie(
        user=user_admin(),
        title="film title select",
        description="film description select",
        photo="photo.png",
        release_date=date(2020,9,1),
        publish_date=date(2020,8,1)
    )


    movies = select_data_movie(user=user, title="film title select", release_date=None, publish_date=None)

    title_filter = filtered_movie(movie, movies)
    assert title_filter.title == "film title select"

    movies = select_data_movie(user=user_admin(),release_date="2020-09-01", title=None, publish_date=None)
    release_date_filter = filtered_movie(movie, movies)
    assert release_date_filter.release_date == date(2020,9,1)

    movies = select_data_movie(user=user_admin(),release_date=None, title=None, publish_date="2020-08-01")
    publish_date_filter = filtered_movie(movie, movies)
    assert publish_date_filter.publish_date == date(2020,8,1)
    
    movies = select_data_movie(user=user_admin(),release_date="2020-09-01", title="film title select", publish_date="2020-08-01")
    multiple = filtered_movie(movie, movies)
    assert multiple.title == "film title select"
    assert multiple.release_date == date(2020,9,1)
    assert multiple.publish_date == date(2020,8,1)


""" Test user admin select movie """
def test_select_data_movie_admin():
    select_data_movie_by_users(user_admin())

""" Test user staff select movie """
def test_select_data_movie_staff():
    select_data_movie_by_users(user_staff())
    