from abc import abstractmethod
from app.movie.repositories.repository import AbstractRepository
from app.movie.domain.entities.user import User

class AbstractUserRepository(AbstractRepository):
    
    @abstractmethod
    def all(self) -> User:
        raise NotImplementedError

    @abstractmethod
    def deleteById(cls, entity_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(cls, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def filterBy(cls, where) -> User:
        raise NotImplementedError

    @abstractmethod
    def checkEmailMustUnique(cls, email: str, id:int = None) -> bool:
        raise NotImplementedError

    @abstractmethod
    def checkUsernameMustUnique(cls, username: str, id:int = None) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def filterByRoleAndLikeEmail(cls, role:str = None, email:str = None) -> list:
        raise NotImplementedError