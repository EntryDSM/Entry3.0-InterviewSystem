from app.models import db
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import datetime

from .interview_data import InterviewData
from .info import Info
from .interview_final import InterviewFinal


class GraduateTypeEnum(Enum):
    WILL = 1
    DONE = 2
    GED = 3


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(32), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    graduate_type = db.Column(db.Enum(GraduateTypeEnum), default=GraduateTypeEnum.WILL)

    # one to one
    info = relationship("Info", uselist=False, backref="user")
    interview_final = relationship("InterviewFinal", uselist=False, backref="user")

    # one to many
    interview_data = relationship("InterviewData", uselist=False, backref="user")
