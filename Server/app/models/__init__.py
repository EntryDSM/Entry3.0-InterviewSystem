from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SQLAlchemy:
    def __init__(self, app, test=False):
        db.init_app(app=app)

        if test is True:
            db.create_all()
