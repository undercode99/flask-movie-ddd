from abc import abstractmethod
from app.movie.repositories.repository import AbstractRepository
from app.movie.domain.entities.movie import Movie

class AbstractMovieRepository(AbstractRepository):
    
    @abstractmethod
    def all(self) -> Movie:
        raise NotImplementedError