from datetime import timedelta


class Config:
    DEBUG = True
    HOST = '0.0.0.0'

    RUN_SETTING = {
        'host': HOST,
        'port': 5000,
        'debug': DEBUG
    }

    SERVICE_NAME = 'entry3.0-interview'
    SECRET_KEY = " erich_hartmann"
    JWT_SECRET_KEY = 'otto_carius'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=3)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
    SQLALCHEMY_ECHO = True