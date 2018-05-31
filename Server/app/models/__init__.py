from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SQLAlchemy:
    def __init__(self, app):
        db.init_app(app=app)
