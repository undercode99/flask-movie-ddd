# Restful API Movie with Flask DDD

[![Build Status](https://app.travis-ci.com/undercode99/flask-movie-ddd.svg?branch=main)](https://app.travis-ci.com/undercode99/flask-movie-ddd)

Simple app restfull api, build with python flask this app already scabelable with the versioning api, and separate layers.

Features:
- Docker environment with compose integrate gunicorn, and nginx web server
- Auth JWT
- Role User
- CRUD Movie
- CRUD User

This apps using the DDD (Domain Driven Design) approach, the application is divided into several parts including

1. **Application layer**

   Inside this application layer is the layer that is responsible for receiving https requests, form validators, http responses, controllers

2. **Domain layers**

   In the domain layer is the layer that is responsible for the apps business, in the domain layer it is divided into services, abstract repositories, entities, and value objects.

3. **Infrastructure layers**

   Is the layer in charge of the 3rd party, including the persistence layer for connection database or query


## Information API

- **Documentation API Postman** :
   
   https://documenter.getpostman.com/view/17611308/UUxwD9rS#7129ccdd-028f-4e30-9484-35bd14f7fd6d 

- **Link Deployed API (Hosted on AWS)** : 

   https://movie-app.usman.id/api 
   
   Auth login:

    username : **admin**
    
    password : **admin123**


## Getting start with docker compose
1. Clone this repository

   ``` git clone https://github.com/undercode99/flask-movie-ddd.git ```

   Enter directory

   ``` cd flask-movie-ddd ```

3. Create file .env and add config database and sekeret key

    Example: 
    ```env
    SQLALCHEMY_DB_CONFIG=sqlite:///database.db
    SECRET_KEY=dhsaydga6d7asda7da
    ```
    if use mysql database config like this
    ```
    SQLALCHEMY_DB_CONFIG=mysql+pymysql://username:password@localhost/name_database
    ```
 4. Running docker compose with command

    ``` docker-compose up --build -d ```

    **-d** is mean running in background, 
    **--build** is mean build all image in yaml compose

5. App already deploy

   Open app with postman with default auth account: 
   - username : admin
   - password : admin123


## Getting start with local machine

1. Clone this repository

   ``` git clone flask-app-ddd.git ```

   Enter directory
   
   ``` cd flask-app-ddd ```

2. Create python env with virtualenv
   
   ``` virtualenv flask-ddd-env ```
  
   Activate virtualenv with command, if you using linux

   ``` source flask-ddd-env/bin/activate ```
   
   If you using windows

   ``` .\flask-ddd-env\Scripts\activate.bat ```
3. Install package 

   ``` pip install -r requirements.txt```

4. Create file .env and add config database and sekeret key

    Example: 
    ```env
    SQLALCHEMY_DB_CONFIG=sqlite:///database.db
    SECRET_KEY=dhsaydga6d7asda7da
    ```
    if use mysql database config like this
    ```
    SQLALCHEMY_DB_CONFIG=mysql+pymysql://username:password@localhost/name_database
    ```

5. Test app with pytest command

    ``` pytest ```

5. Migrate database and generate user

   ``` python migrate.py ```

   ``` python generate_user.py ```

6. Runing application 

   ``` python serve.py ```

   Open app with postman with default auth account: 
   - username : admin
   - password : admin123



