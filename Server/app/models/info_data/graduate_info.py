from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.models.info_data.enum import StatusEnum


class GraduateInfo(db.Model):
    __tablename__ = 'graduate_info'

    graduate_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'))
    grade_n = db.Column(Integer(unsigned=True))
    class_n = db.Column(Integer(unsigned=True))
    number_n = db.Column(Integer(unsigned=True))
    school_name = db.Column(db.VARCHAR)
    school_code = db.Column(db.VARCHAR)
    status = db.Column(db.Enum(StatusEnum))
    graduate_year = db.Column(Integer(unsigned=True))
