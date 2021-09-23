from datetime import date
from app.movie.domain.entities.entity import Entity

class Movie(Entity):
    def __init__(
        self, id: int = None, title: str = None, description: str = None, photo: str = None, release_date: date = None, publish_date: date = None
    ):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.photo: str = photo
        self.release_date: date = release_date
        self.publish_date: date = publish_date

    @staticmethod
    def fromObject(obj):
        return Movie(
            id=obj.id,
            title=obj.title,
            description=obj.description,
            photo=obj.photo,
            release_date=obj.release_date,
            publish_date=obj.publish_date
        )

    def toDict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "photo": "/storage/"+self.photo, "release_date": self.release_date.strftime("%Y-%m-%d"), "publish_date": self.publish_date.strftime("%Y-%m-%d") }


    def __repr__(self):
        return f"<Movie {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)