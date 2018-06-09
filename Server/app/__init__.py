from flask import Flask
from flask_jwt_extended import JWTManager

from app.views import Router, after_request
from app.models import SQLAlchemy


def create_app(*config_cls, test=False):
    """
    Creates Flask instance & initialize
    Returns:
        Flask
    """
    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    JWTManager(app_)
    SQLAlchemy(app_, test)
    Router(app_)

    app_.after_request(after_request)

    return app_