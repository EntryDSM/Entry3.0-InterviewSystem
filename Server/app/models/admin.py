from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum


class AdminTypeEnum(Enum):
    ROOT = 1
    ADMINISTRATION = 2
    QUESTION = 3
    INTERVIEW = 4


class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(200))
    admin_type = db.Column(db.Enum(AdminTypeEnum))
    name = db.Column(db.VARCHAR(4))
