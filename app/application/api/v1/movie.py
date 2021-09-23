from flask import request
from werkzeug.utils import secure_filename
from datetime import date
from app.application.http.response import Response
from app.application.http.middleware import token_required
from app.application.validator.movie import create_movie_validate, update_movie_validate, to_date
from app.movie.services.movie_service import create_new_movie, update_data_movie, delete_data_movie, select_data_movie
import json
from .base import api_v1
import os
import uuid

@api_v1.route("/movies")
@token_required
def movies(user):
    data = [ item.toDict() for item in select_data_movie(
        user=user,
        title=request.args.get("title"),
        release_date=request.args.get("release_date"),
        publish_date=request.args.get("publish_date"),
    )]
    return Response({"data" : data }).send()


@api_v1.route("/movies", methods=["POST"])
@token_required
def create_movie(user):
    try:
        data = request.form.to_dict()
        validate = create_movie_validate(data)
        if validate['isError'] :
            return Response().badRequest(message="Failed to create movie", errorMessage=validate['message'])
        
        errResponse =  Response().badRequest(message="Failed to create movie", errorMessage="Must fill photo movie")
        if 'photo' not in request.files:
            return errResponse
        if request.files['photo'].filename == '':
            return errResponse
        
        storage = "./storage"
        if not os.path.exists(storage):
            os.mkdir(storage)

        image = request.files['photo']
        image_name = str(uuid.uuid4())+"-"+secure_filename( image.filename)
        image.save(os.path.join(storage, image_name))
        
        data = create_new_movie(
            user=user, 
            title=data["title"],
            photo=image_name,
            description=data["description"],
            publish_date=to_date(data["publish_date"]),
            release_date=to_date(data["release_date"]),
        )

        return Response({ "data": data.toDict()}).created()
    except Exception as e:
         return Response().serverError(message="Failed to create movie", errorMessage=str(e))

@api_v1.route("/movies/<int:id>", methods=["PUT"])
@token_required
def update_movie(user, id):
    try:
        data_form = request.form
        validate = update_movie_validate(data_form.to_dict())
        if(validate['isError']):
            return Response().badRequest(message="Failed to update movie", errorMessage=validate['message'])
        
        image_name = ""
        storage = "./storage"
        if 'photo' in request.files:
            if request.files['photo'].filename != '':
                if not os.path.exists(storage):
                    os.mkdir(storage)
                    print("Creating directory uploads")

                image = request.files['photo']
                image_name = str(uuid.uuid4())+"-"+secure_filename( image.filename)
                image.save(os.path.join(storage, image_name))

        data = update_data_movie(
            user=user,
            id=id,
            title=data_form.get("title", ""),
            description=data_form.get("description", ""),
            photo=image_name,
            release_date= to_date(data_form.get("release_date")) if data_form.get("release_date") is not  None else "",
            publish_date= to_date(data_form.get("publish_date")) if data_form.get("publish_date") is not  None else ""
        )
        return Response({ "data": data.toDict(), "message": "Update movie success"}).send()
    except Exception as e:
        return Response().serverError(message="Failed to update movie", errorMessage=str(e))




@api_v1.route("/movies/<int:id>", methods=["DELETE"])
@token_required
def delete_movie(user, id):
    try:
        movie = delete_data_movie(user, id)
        os.remove("storage/"+movie.photo)
        return Response({"data": movie.toDict(), "message": "Delete movie success"}).send()
    except Exception as e:
        return Response().serverError(message="Failed to delete movie", errorMessage=str(e))

