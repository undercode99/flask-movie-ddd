import sys
import os
from datetime import datetime, date
import enum
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_utils.function import database_exists
import sqlalchemy_utils
import os
from dotenv import load_dotenv
load_dotenv()


db_config = os.getenv('SQLALCHEMY_DB_CONFIG') 
ENGINE = create_engine(
    db_config,
    encoding="utf-8",
    echo=True
)


print("Hellpppp")

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()



class RoleEnum(enum.Enum):
    staff = "staff"
    admin = "admin"

class UserModel(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(200), unique=True)
    email = Column('email', String(200), unique=True)
    password = Column('password', String(200))
    fullname = Column('fullname', String(200))
    role = Column('role', String(200))
    created_at = Column('created_at', DATETIME, default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DATETIME, default=datetime.now, nullable=False)

    def __init__(self, username: str, password: str, fullname: str, email: str, role: str):
        self.username: str = username
        self.password: str = password
        self.fullname: str = fullname
        self.email: str = email
        self.role: str = role


class MovieModel(Base):
    __tablename__ = "movie"
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(200))
    description = Column('description', Text)
    photo = Column('photo', String(200))
    release_date = Column('release_date', DATE)
    publish_date = Column('publish_date', DATE)
    created_at = Column('created_at', DATETIME, default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DATETIME, default=datetime.now, nullable=False)

    def __init__(self, title: str, description: str, photo: str, release_date: date, publish_date: str):
        self.title: str = title
        self.description: str = description
        self.photo: str = photo
        self.release_date: date = release_date
        self.publish_date: date = publish_date

def auto_create_table():
    Base.metadata.create_all(bind=ENGINE)
