"""
File Description: This file is the main file of the api package. It is responsible for creating the Flask app and the database. It also registers the blueprints for the auth routes.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from os import path
from env.passwords import *
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    # for database initialization
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # for jwt (json web token ) token
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    jwt = JWTManager(app)

    from .project import project
    from .auth import auth
    from .users import users
    from .userData import userData

    app.register_blueprint(project, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(users, url_prefix="/")
    app.register_blueprint(userData, url_prefix="/")

    # import models database
    from .models import (
        Canidate,
        Recruiter,
        InnovationChallenge,
        canidateTeams,
        canidateToTeam,
    )

    CORS(app)  # Enable CORS for all routes
    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists("api/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
