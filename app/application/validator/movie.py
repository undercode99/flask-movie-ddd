from cerberus import Validator
from datetime import datetime

to_date = lambda s: datetime.strptime(s, "%Y-%m-%d")

def create_movie_validate(document):

    schema = {
        "title" : {"required": True, "type": "string", "maxlength": 200, "minlength": 5},
        "description" : {"required": True, "type": "string", "maxlength": 1000, "minlength": 5},
        "release_date" : {"required": True,"type": "datetime","coerce": to_date},
        "release_date"  : {"required": True, "type": "datetime","coerce": to_date}
    }

    v = Validator(purge_unknown=True)
    if(v.validate(document, schema) == False):
        return {
            "isError": True,
            "message": v.errors
        }
    return { "isError": False }


def update_movie_validate(document):
    schema = {
        "title" : {"type": "string", "maxlength": 200, "minlength": 5},
        "description" : {"type": "string", "maxlength": 1000, "minlength": 5},
        "release_date" : {"type": "datetime","coerce": to_date},
        "release_date"  : { "type": "datetime","coerce": to_date}
    }

    v = Validator(purge_unknown=True)
    if(v.validate(document, schema) == False):
        return {
            "isError": True,
            "message": v.errors
        }
    return { "isError": False }
