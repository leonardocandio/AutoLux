import os
from dotenv import load_dotenv, find_dotenv



class Config:
    # Enabling development environment
    load_dotenv(find_dotenv())

    FLASK_ENV = "development"
    SECRET_KEY = "secretkey"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    PORT = 5001

    # Sign in with Google
    # GOOGLE = {
    #     'consumer_key': os.getenv("GOOGLE_CLIENT_ID"),
    #     'consumer_secret': os.getenv("GOOGLE_CLIENT_SECRET")
    # }
    

    # Flask-Caching related configs
    CACHE_TYPE: 'SimpleCache'  
    CACHE_DEFAULT_TIMEOUT: 300

    # Application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Database definition
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    FLASK_DEBUG = True
    TESTING = True


class Test(Config):
    pass


class Production(Config):
    pass
