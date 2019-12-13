# /src/config.py

import os

user = 'test'
password = 'password'
host = 'localhost'
database = 'blog_api_db'
port = '5432'
JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
DATABASE_URL = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

class Development(object):
    """
    Development environment configuration
    """

    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    #JWT_SECRET_KEY = JWT_SECRET_KEY

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
   # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
   # JWT_SECRET_KEY = JWT_SECRET_KEY

app_config = {
    'development': Development,
    'production': Production,
}