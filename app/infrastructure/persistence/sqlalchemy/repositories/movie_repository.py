from app.movie.domain.entities.movie import Movie
from app.movie.repositories.movie_repository import AbstractMovieRepository
from app.infrastructure.persistence.sqlalchemy.models import session, MovieModel
from datetime import date

class MovieSqlAlchemyRepository(AbstractMovieRepository):

    @classmethod
    def get(cls, entity_id: int) -> Movie:
        result: MovieModel = session.query(MovieModel).get(entity_id)
        if(result == None):
            raise Exception("Movie not found with id {}".format(entity_id))
        return Movie.fromObject(result)

    @classmethod
    def deleteById(cls, entity_id: int) -> Movie:
        try:
            movie = MovieModel.query.filter_by(id=entity_id).one()
            session.delete(movie)
            session.commit()
            return Movie.fromObject(movie)
        except Exception as e:
            session.rollback()
            raise ValueError(str(e))
        

    @classmethod
    def add(cls, movie: Movie) -> Movie:
        try:
            model = MovieModel(title=movie.title,description=movie.description, photo=movie.photo, release_date=movie.release_date, publish_date=movie.publish_date)
            session.add(model)
            session.commit()
            session.flush()
            return movie.fromObject(model)
        except: 
            session.rollback()
            raise ValueError(str(e))

    @classmethod
    def all(cls) -> list:
        try:
            rows: list = session.query(MovieModel).all()
            return [Movie.fromObject(row) for row in rows ]
        except Exception as e:
            session.rollback()
            raise ValueError(str(e))

    
    @classmethod
    def update(cls, movie: Movie) -> Movie:

        update = {}
        if movie.title != "":
            update[MovieModel.title] = movie.title
        if movie.description != "":
            update[MovieModel.description] = movie.description
        if movie.release_date != "":
            update[MovieModel.release_date] = movie.release_date
        if movie.photo != "":
            update[MovieModel.photo] = movie.photo
        if movie.publish_date != "":
            update[MovieModel.publish_date] = movie.publish_date
        try:
            session.query(MovieModel)\
            .filter(MovieModel.id  == movie.id )\
            .update(update)
            session.commit()
            return cls.get(movie.id)

        except Exception as e:
            session.rollback()
            raise ValueError(str(e))

    
    @classmethod
    def filterMovieByTitleReleasePublish(cls, title:str = None, release_date:date = None, publish_date:date = None) -> list:
        try:
            query = session.query(MovieModel)
            if title:
                query = query.filter(MovieModel.title.like(f'%{title}%'))
            if release_date:
                query = query.filter(MovieModel.release_date == release_date)
            if publish_date:
                query = query.filter(MovieModel.publish_date == publish_date)

            rows: list = query.all()
            return [Movie.fromObject(row) for row in rows ]
        except Exception as e:
            session.rollback()
            raise ValueError(str(e))

