from app.movie.domain.entities.user import User
from app.movie.repositories.user_repository import AbstractUserRepository
from app.infrastructure.persistence.sqlalchemy.models import session, UserModel
from sqlalchemy import and_

class UserSqlAlchemyRepository(AbstractUserRepository):

    @classmethod
    def get(cls, entity_id: int) -> User:
        result: UserModel = session.query(UserModel).get(entity_id)
        if(result == None):
            raise Exception("User not found with id {}".format(entity_id))
        return User.fromObject(result)

    @classmethod
    def deleteById(cls, entity_id: int):
        user = UserModel.query.filter_by(id=entity_id).one()
        session.delete(user)
        session.commit()
        return User.fromObject(user)

    
    @classmethod
    def add(cls, user: User) -> User:
        models = UserModel(fullname=user.fullname, email=user.email, password=user.password, username=user.username, role=user.role.value)
        session.add(models)
        session.commit()
        session.flush()
        return User.fromObject(models)

    @classmethod
    def all(cls) -> list:
        rows: list = session.query(UserModel).all()
        return [User.fromObject(row) for row in rows ]

    @classmethod
    def update(cls, user: User) -> User:
        update = {}
        if user.email != "":
            update[UserModel.email] = user.email
        if user.password != "":
            update[UserModel.password] = user.password
        if user.fullname != "":
            update[UserModel.fullname] = user.fullname
        if user.username != "":
            update[UserModel.username] = user.username
        session.query(UserModel)\
        .filter(UserModel.id  == user.id )\
        .update(update)
        session.commit()
        return cls.get(user.id)

    @classmethod
    def filterBy(cls, where) -> User:
        result = session.query(UserModel).filter_by(**where).first()
        if result is None:
            return None
        return User.fromObject(result)

    @classmethod
    def checkEmailMustUnique(cls, email: str, id:int = None) -> bool:
        query = session.query(UserModel)
        if id is None:
            query = query.filter(UserModel.email == email)
        else:
            query = query.filter(UserModel.id != id, UserModel.email == email)
        if query.first() is None:
            return True
        return None

    @classmethod
    def checkUsernameMustUnique(cls, username: str, id:int = None) -> bool:
        query = session.query(UserModel)
        if id is None:
            query = query.filter(UserModel.username == username)
        else:
            query = query.filter(UserModel.id != id, UserModel.username == username)
        if query.first() is None:
            return True
        return None
    
    @classmethod
    def filterByRoleAndLikeEmail(cls, role:str = None, email:str = None) -> list:
        query = session.query(UserModel)
        if email and role:
            query = query.filter(UserModel.email.like(f'%{email}%'), UserModel.role == role)
        elif role != None and email == None:
            query = query.filter(UserModel.role == role)
        elif email != None and role == None:
            query = query.filter(UserModel.email.like(f'%{email}%'))

        rows: list = query.all()
        return [User.fromObject(row) for row in rows ]

    