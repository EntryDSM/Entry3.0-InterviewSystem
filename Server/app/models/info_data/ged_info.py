from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.models.info_data.enum import StatusEnum


class GedInfo(db.Model):
    __tablename__ = 'graduate_info'

    ged_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer)
    status = db.Column(db.Enum(StatusEnum))
