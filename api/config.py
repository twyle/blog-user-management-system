# -*- coding: utf-8 -*-
"""This module contain the confuguration for the application."""
import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Configuration used during development."""

    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    DEBUG = True
    TESTING = False

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    EMAIL_MAX_LENGTH = int(os.getenv("EMAIL_MAX_LENGTH", "64"))
    EMAIL_MIN_LENGTH = int(os.getenv("EMAIL_MIN_LENGTH", "8"))

    NAME_MAX_LENGTH = int(os.getenv("NAME_MAX_LENGTH", "20"))
    NAME_MIN_LENGTH = int(os.getenv("NAME_MIN_LENGTH", "2"))

    PASSWORD_MAX_LENGTH = int(os.getenv("PASSWORD_MAX_LENGTH", "20"))
    PASSWORD_MIN_LENGTH = int(os.getenv("PASSWORD_MIN_LENGTH", "3"))


class TestingConfig(BaseConfig):
    """Configuration used during testing."""

    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    DEBUG = True
    TESTING = True

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(BaseConfig):
    """Configuration used during staging."""

    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    DEBUG = False
    TESTING = False

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    """Configuration used during production."""

    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    DEBUG = False
    TESTING = False

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


Config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}