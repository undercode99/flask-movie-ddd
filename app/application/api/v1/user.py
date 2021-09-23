from flask import request
from app.application.http.response import Response
from app.application.http.middleware import token_required
from app.application.validator.user import create_user_validate, update_user_validate, auth_login_validate
from app.movie.services.user_service import create_new_user, select_all_user, update_data_user, filter_role_and_email, delete_data_user
import json
from .base import api_v1



@api_v1.route("/users")
@token_required
def users(user):
    data = [ item.toDict() for item in filter_role_and_email(user=user, email=request.args.get("email"), role=request.args.get("role"))]
    return Response({"data" : data }).send()


@api_v1.route("/users", methods=["POST"])
@token_required
def create_user(user):
    try:
        data = request.form.to_dict()
        validate = create_user_validate(data)
        if(validate['isError']):
            return Response().badRequest(message="Failed to create user", errorMessage=validate['message'])
        data = create_new_user(user=user, fullname=data["fullname"], email=data["email"], username=data["username"], password=data["password"], role=data["role"])
        return Response({ "data": data.toDict()}).created()
    except Exception as e:
         return Response().serverError(message="Failed to create user", errorMessage=str(e))


@api_v1.route("/users/<int:id>", methods=["PUT"])
@token_required
def update_user(user, id):
    try:
        data_form = request.form
        validate = update_user_validate(data_form.to_dict())
        if(validate['isError']):
            return Response().badRequest(message="Failed to update user", errorMessage=validate['message'])
        data = update_data_user(
            user=user,
            id=id,
            fullname=data_form.get("fullname", ""),
            email=data_form.get("email", ""),
            username=data_form.get("username", ""),
            password=data_form.get("password", ""),
            role=data_form.get("role", "")
        )
        return Response({ "data": data.toDict(), "message": "Update user success"}).send()
    except Exception as e:
        return Response().serverError(message="Failed to update user", errorMessage=str(e))



@api_v1.route("/users/<int:id>", methods=["DELETE"])
@token_required
def delete_user(user, id):
    try:
        user = delete_data_user(user, id)
        return Response({"data": user.toDict(), "message": "Delete user success"}).send()
    except Exception as e:
        return Response().serverError(message="Failed to delete user", errorMessage=str(e))

