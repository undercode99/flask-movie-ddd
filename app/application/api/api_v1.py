from flask import Blueprint
from app.application.http.response import Response
api_v1 = Blueprint("api_version1", __name__)

@api_v1.route("/movie")
def movie():
    return Response({ "data": "movie data" }).send()


@api_v1.route("/user")
def user():
    return "user data"