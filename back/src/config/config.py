from decouple import config


class Config:
    DEBUG = config('DEBUG')
    TESTING = config('TESTING')
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')


