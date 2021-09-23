import os
import jwt
from datetime import datetime,timedelta
from flask import request
from app.application.http.response import Response
from app.application.validator.user import auth_login_validate
from app.movie.services.auth_services import check_user_password
from .base import api_v1


@api_v1.route("/auth/login", methods=["POST"])
def auth_login():
    try:
        data = request.form
        validate = auth_login_validate(data.to_dict())
        if validate['isError']:
            return Response().badRequest(errorMessage=validate["message"])
            
        user = check_user_password(data.get('password'), data.get('username').lower())
        token = jwt.encode({
            'sub': user.id,
            'fullname': user.fullname,
            'username': user.username,
            'email': user.email,
            'role': user.role.value,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=120)
        }, os.getenv("SECRET_KEY"),  algorithm="HS256")

        return Response({
            "data": user.toDict(),
            "token": token
        }).send()

    except Exception as e:
        return Response().unauthorized(errorMessage=str(e))

