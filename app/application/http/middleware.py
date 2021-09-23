import jwt
from .response import Response
from flask import request, current_app
from functools import wraps
from app.movie.services.auth_services import check_user_exists
import os



def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        error_response = {
            'authenticated': False,
            'error': True,
            'responseCode' : 401
        }
        
        invalid_msg = {
            'message': 'Invalid token. Reauthentication required',
            **error_response
        }

        nothave_headers_msg = {
            'message': 'Required token authentication',
            **error_response
        }

        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            **error_response
        }


        try:
            auth_headers = request.headers.get('Authorization')
            if auth_headers is None:
                return Response(nothave_headers_msg).send()

            token = auth_headers.split()[1]
            data = jwt.decode(token,os.getenv("SECRET_KEY"), algorithms=["HS256"])
            user = check_user_exists(id=data['sub'])
            if not user:
                raise ValueError('User not found')
            return f(user, *args, **kwargs)

        except jwt.ExpiredSignatureError as e:
            expired_msg['errorMessage'] = str(e)
            return Response(expired_msg).send()

        except jwt.InvalidTokenError as e:
            invalid_msg['errorMessage'] = str(e)
            return Response(invalid_msg).send()

        except Exception as e:
           invalid_msg['errorMessage'] = str(e)
           return Response(invalid_msg).send()

    return _verify
