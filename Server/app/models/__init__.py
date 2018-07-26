from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SQLAlchemy:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app=app)

        if app.config["DEBUG"] is True:
            # db.drop_all(app=app)
            db.create_all(app=app)
