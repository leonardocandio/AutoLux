import os
from dotenv import load_dotenv, find_dotenv


class Config:
    # Enabling development environment
    load_dotenv(find_dotenv())
    FLASK_DEBUG = True
    TESTING = True
    SECRET_KEY = "secretkey"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-Caching related configs
    CACHE_TYPE: 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT: 300

    # Application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Database definition
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
