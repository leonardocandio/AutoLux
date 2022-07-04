import os

from dotenv import load_dotenv, find_dotenv


class Config:
    # Enabling development environment
    load_dotenv(find_dotenv())
    FLASK_DEBUG = True
    TESTING = True
    SECRET_KEY = '\x14\x86\r\x99\x1a\xf5DN\x87bg\x98\xa9\x03\x1f\x91\x8fVUT\xd0WT \x8b\x8e3\xd6bj\x8c+'
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


class ConfigTest(Config):
    LOGIN_DISABLED = True

    FLASK_ENV = "production"

    # Database definition
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI_TEST")
