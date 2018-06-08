from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from .enum import AdminTypeEnum


class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    email = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    admin_type = db.Column(db.Enum(AdminTypeEnum))