from datetime import date
from app.movie.domain.entities.movie import Movie
from app.movie.domain.entities.user import User
from app.infrastructure.persistence.sqlalchemy.repositories.movie_repository import MovieSqlAlchemyRepository
from app.movie.services.auth_services import check_authorization

def create_new_movie(user: User, title: str, description: str, photo: str, release_date: date, publish_date: date) -> Movie:
    """ Auth services """
    check_authorization(user, "add_movie")
    
    movie = MovieSqlAlchemyRepository.add(
        Movie(
            title=title,
            description=description,
            photo=photo,
            release_date=release_date,
            publish_date=publish_date
        )
    )
    return movie

def update_data_movie(user: User, id: int, title: str, description: str, photo: str, release_date: date, publish_date: date):
    """ Auth services """
    check_authorization(user, "edit_movie")
    movie = Movie(
        id=id,
        title=title,
        description=description,
        photo=photo,
        release_date=release_date,
        publish_date=publish_date
    )
    return MovieSqlAlchemyRepository.update(movie)



def select_data_movie(user: User, title: str, release_date: date, publish_date: date) -> Movie:
    check_authorization(user, "read_movie")
    return MovieSqlAlchemyRepository.filterMovieByTitleReleasePublish(title, release_date, publish_date)



def delete_data_movie(user: User, movie_id: int) -> Movie:
    """ Auth services """
    check_authorization(user, "delete_movie")
    return MovieSqlAlchemyRepository.deleteById(movie_id)