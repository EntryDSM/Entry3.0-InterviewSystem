from datetime import timedelta


class Config:
    DEBUG = True
    HOST = 'localhost'

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

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:wasitacatisaw?@localhost:3333/entry"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:wasitacatisaw?@localhost:3333/"+SERVICE_NAME
    SQLALCHEMY_ECHO = True

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'Interview System'
        },
        'basePath': '/ '
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Some Tag',
                'description': 'Some API'
            }
        ]
    }