from datetime import date
from app.movie.domain.entities.entity import Entity
from app.movie.domain.value_object.roles import Roles

class User(Entity):
    def __init__(
        self,  username: str, password: str, fullname: str, email: str, role: Roles = None, id: int = None
    ) -> None:
        self.id: int = id
        self.username: str = username
        self.password: str = password
        self.fullname: str = fullname
        self.email: str = email
        self.role: Roles = Roles(role)

    @staticmethod
    def fromObject(obj):
        return User(
            id=obj.id,
            username=obj.username,
            password=obj.password,
            fullname=obj.fullname,
            email=obj.email,
            role=Roles(obj.role)
        )

    def toDict(self):
        return {"id": self.id, "fullname": self.fullname, "username": self.username, "email": self.email, "role": self.role.value, "password": self.password }


    def __repr__(self):
        return f"<User {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)