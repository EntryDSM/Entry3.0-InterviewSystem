from app.models import db
import datetime
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum


class GenderEnum(Enum):
    M = 0,
    F = 1


class Info(db.Model):
    __tablename__ = "info"

    info_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    user_id = db.Column(Integer(unsigned=True), db.ForeignKey('user.user_id'))
    address_base = db.Column(db.VARCHAR)
    address_detail = db.Column(db.VARCHAR)
    region = db.Column(db.VARCHAR)
    name = db.Column(db.VARCHAR)
    sex = db.Column(db.Enum(GenderEnum))
    parent_name = db.Column(db.VARCHAR)
    parent_tel = db.Column(db.VARCHAR)
    my_tel = db.Column(db.VARCHAR)
    student_code = db.Column(db.VARCHAR)
    introduce = db.Column(db.VARCHAR)
    study_plan = db.Column(db.VARCHAR)
    img_path = db.Column(db.VARCHAR)
    create_at = db.Column(db.TIMESTAMP)
    update_at = db.Column(db.Date, onupdate=datetime.datetime.now().date())
