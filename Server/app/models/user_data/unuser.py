from app.models import db


class UnUser(db.Model):
    __tablename__ = 'unuser'

    code = db.Column(db.VARCHAR, unique=True)
    email = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
