from enum import Enum, unique

@unique
class Roles(Enum):

    Admin = "admin"
    Staff = "staff"
    Null = ""

    def __new__(cls, value, *arg):
        obj = object.__new__(cls)
        obj._value = value
        return obj

    def __init__(self, *args):
        self.values = args


class ServicesRole():
    data_roles = {
        "staff": ["edit_movie","read_movie"],
        "admin": [
            "read_movie",
            "add_movie",
            "edit_movie",
            "delete_movie",
            "add_user",
            "edit_user",
            "delete_user",
            "read_user"
        ]
    }

    @classmethod
    def roles(cls, role):
        if role not in cls.data_roles:
            return []
        return cls.data_roles[role]
