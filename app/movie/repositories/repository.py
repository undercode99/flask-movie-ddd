from abc import ABC, abstractmethod
from app.movie.domain.entities.entity import Entity

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_id) -> Entity:
        raise NotImplementedError