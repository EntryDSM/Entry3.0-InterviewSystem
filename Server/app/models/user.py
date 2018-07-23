from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum
import time

class GraduateTypeEnum(Enum):
    WILL = 1
    DONE = 2
    GED = 3


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(32), primary_key=True)
    create_at = db.Column(db.TIMESTAMP, default=time.time)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    graduate_type = db.Column(db.Enum(GraduateTypeEnum), default=GraduateTypeEnum.WILL)