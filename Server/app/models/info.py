from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum
from datetime import datetime


class AdmissionEnum(Enum):
    NORMAL = 1
    MEISTER = 2
    SOCIAL = 3


class AdmissionDetailEnum(Enum):
    DEFAULT = 0
    BENEFICIARY = 1
    ONE_PARENT = 2
    CHA_UPPER = 3
    CHACHA_UPPER = 4
    FROM_NORTH = 5
    MULTI_CULTURE = 6
    ETC = 7


class SexEnum(Enum):
    FEMALE = 1
    MALE = 2


class Info(db.Model):
    __tablename__ = "info"

    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id", ondelete='CASCADE'), primary_key=True)
    address_base = db.Column(db.String(100), default="", nullable=False)
    address_detail = db.Column(db.String(50), default="", nullable=False)
    admission = db.Column(db.Enum(AdmissionEnum), default=AdmissionEnum.NORMAL)
    admission_detail = db.Column(db.Enum(AdmissionDetailEnum), default=AdmissionDetailEnum.DEFAULT)
    region = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(20), default="", nullable=False)
    sex = db.Column(db.Enum(SexEnum))
    parent_name = db.Column(db.String(20), default="", nullable=False)
    parent_tell = db.Column(db.String(15), default="", nullable=False)
    my_tel = db.Column(db.String(15), default="", nullable=False)
    introduce = db.Column(db.String(1600), default="", nullable=False)
    study_plan = db.Column(db.String(1600), default="", nullable=False)
    img_path = db.Column(db.String(50), unique=True)
    exam_code = db.Column(db.String(6), unique=True)
    create_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, default=datetime.now())
    receipt_code = db.Column(Integer(display_width=3, unsigned=True, zerofill=True), unique=True, autoincrement=True)
