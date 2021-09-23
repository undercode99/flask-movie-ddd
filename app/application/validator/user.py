from cerberus import Validator


def create_user_validate(document):
    schema = {
        "username" : {"required": True, "type": "string", "maxlength": 200, "minlength": 5},
        "fullname" : {"required": True, "type": "string", "maxlength": 200, "minlength": 5},
        "email"    : {"required": True, "type": "string", "maxlength": 200, "minlength": 5},
        "password" : {"required": True, "type": "string", "minlength": 8},
        "role"     : {"required": True, "type": "string", 'allowed': ['admin', 'staff']}
    }

    v = Validator(purge_unknown=True)
    if(v.validate(document, schema) == False):
        return {
            "isError": True,
            "message": v.errors
        }
    return { "isError": False }


def update_user_validate(document):
    schema = {
        "username" : {"type": "string", "maxlength": 200, "minlength": 5},
        "fullname" : {"type": "string", "maxlength": 200, "minlength": 5},
        "email"    : {"type": "string", "maxlength": 200, "minlength": 5},
        "password" : {"type": "string", "minlength": 8},
        "role"     : {"type": "string", 'allowed': ['admin', 'staff']}
    }

    v = Validator(purge_unknown=True)
    if(v.validate(document, schema) == False):
        return {
            "isError": True,
            "message": v.errors
        }
    return { "isError": False }

def auth_login_validate(document):

    schema = {
        'username': {'required': True, 'type': 'string'},
        'password': {'required': True, 'type': 'string'}
    }

    v = Validator(purge_unknown=True)
    if(v.validate(document, schema) == False):
        return {
            "isError": True,
            "message": v.errors
        }
    return { "isError": False }
