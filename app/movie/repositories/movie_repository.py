from abc import abstractmethod
from app.movie.repositories.repository import AbstractRepository
from app.movie.domain.entities.movie import Movie
from datetime import date

class AbstractMovieRepository(AbstractRepository):
    
    @abstractmethod
    def all(self) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def deleteById(cls, entity_id: int) -> Movie:
        raise NotImplementedError
        
    @abstractmethod
    def update(cls, movie: Movie) -> Movie:
        raise NotImplementedError
    
    @classmethod
    def filterMovieByTitleReleasePublish(cls, title:str = None, release_date:date = None, publish_date:date = None) -> list:
        raise NotImplementedError
        