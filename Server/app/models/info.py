from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum
from datetime import datetime
import time


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


class Info(db.Model):
    __tablename__ = "info"

    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id"), primary_key=True)
    address_base = db.Column(db.String(100), default="")
    address_detail = db.Column(db.String(50), default="")
    admission = db.Column(db.Enum(AdmissionEnum), default=AdmissionEnum.NORMAL)
    admission_detail = db.Column(db.Enum(AdmissionDetailEnum), default=AdmissionDetailEnum.DEFAULT)
    region = db.Column(db.Boolean(), default=False)
    name = db.Column(db.String(12), default="")
    sex = db.Column(db.Boolean(), default=True)
    parent_name = db.Column(db.String(12), default="")
    parent_tell = db.Column(db.String(20), default="")
    my_tel = db.Column(db.String(20), default="")
    introduce = db.Column(db.Text(1600), default="")
    study_plan = db.Column(db.Text(1600), default="")
    img_path = db.Column(db.String(50), unique=True, default="")
    exam_code = db.Column(db.String(6), default="", unique=True)
    create_at = db.Column(db.TIMESTAMP, default=time.time())
    update_at = db.Column(db.TIMESTAMP, default=time.time())
    receipt_code = db.Column(Integer(display_width=3, unsigned=True, zerofill=True), unique=True, autoincrement=True)
