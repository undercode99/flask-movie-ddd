"""
__init_.py
- creates a Flask app instance
"""
import os
from dotenv import load_dotenv
load_dotenv()

from app.infrastructure.persistence.sqlalchemy.models import auto_create_table
from app.application.api import register_api
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from distutils.util import strtobool


def create_app(app_name='MOVIE_RESTFULAPI'):

  """ 
    Instance app flask
  """
  app = Flask(app_name, static_folder='storage')
  app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
  app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


  """"
    CORS application for api endpoint
    with orgin any
  """
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  """ 
    Instance app database model  
  """
  auto_create_table()

  """
    Register liste api
  """
  register_api(app)

  return app
