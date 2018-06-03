from app.models import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, db.ForeignKey("unuser.code"), primary_key=True)
    email = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    create_at = db.Column(db.TIMESTAMP)

