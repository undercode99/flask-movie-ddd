from abc import abstractmethod
from app.movie.repositories.repository import AbstractRepository
from app.movie.domain.entities.user import User

class AbstractUserRepository(AbstractRepository):
    
    @abstractmethod
    def all(self) -> User:
        raise NotImplementedError
    
