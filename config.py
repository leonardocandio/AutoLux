import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    # Enabling development environment

    FLASK_ENV = "development"
    SECRET_KEY = "secretkey"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    PORT = 5001

    # Application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Database definition
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    TESTING = True


class Test(Config):
    pass


class Production(Config):
    pass
