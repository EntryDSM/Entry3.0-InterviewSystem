from app.models import db
from sqlalchemy.orm import relationship
from enum import Enum
from .interview_data import InterviewData


class AdminTypeEnum(Enum):
    ROOT = 1
    ADMINISTRATION = 2
    QUESTION = 3
    INTERVIEW = 4


class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    admin_type = db.Column(db.Enum(AdminTypeEnum), default=AdminTypeEnum.INTERVIEW)
    name = db.Column(db.String(4), nullable=False)

    # one to many
    interview_data = relationship("InterviewData")