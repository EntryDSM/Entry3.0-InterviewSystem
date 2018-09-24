from datetime import datetime
from enum import Enum

from sqlalchemy.dialects.mysql import INTEGER as Integer

from app.models import db


class AdmissionChoice(Enum):
    NORMAL = 1
    MEISTER = 2
    SOCIAL = 3


class AdmissionDetailChoice(Enum):
    DEFAULT = 0
    BENEFICIARY = 1
    ONE_PARENT = 2
    CHA_UPPER = 3
    CHACHA_UPPER = 4
    FROM_NORTH = 5
    MULTI_CULTURE = 6
    ETC = 7
    # NATIONAL_MERIT = 8
    # SPECIAL_ADMISSION = 9


class SexChoice(Enum):
    FEMALE = 1
    MALE = 2


class InfoModel(db.Model):
    __tablename__ = 'info'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    address_base = db.Column(db.String(100), nullable=False, default="")
    address_detail = db.Column(db.String(50), nullable=False, default="")
    admission = db.Column(db.Enum(AdmissionChoice), nullable=False, default=AdmissionChoice.NORMAL)
    admission_detail = db.Column(db.Enum(AdmissionDetailChoice), nullable=False, default=AdmissionDetailChoice.DEFAULT)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    exam_code = db.Column(db.String(6), nullable=True, unique=True)
    img_path = db.Column(db.String(50), nullable=True, unique=True)
    introduce = db.Column(db.String(1600), nullable=False, default="")
    my_tel = db.Column(db.String(15), nullable=False, default="")
    name = db.Column(db.String(20), nullable=False, default="")
    parent_name = db.Column(db.String(20), nullable=False, default="")
    parent_tel = db.Column(db.String(15), nullable=False, default="")
    region = db.Column(db.Boolean, nullable=False, default=False)
    sex = db.Column(db.Enum(SexChoice))
    study_plan = db.Column(db.String(1600), nullable=False, default="")
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    receipt_code = db.Column(Integer(display_width=3, zerofill=True, unsigned=True),
                             unique=True, nullable=False, autoincrement=True)
