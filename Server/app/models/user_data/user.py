from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(Integer(unsigned=True), primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    create_at = db.Column(db.TIMESTAMP)

