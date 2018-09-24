from datetime import datetime
from enum import Enum

from sqlalchemy.orm import relationship

from app.models import db


class GraduateChoice(Enum):
    WILL = 1
    DONE = 2
    GED = 3


class TempUserModel(db.Model):
    __tablename__ = 'temp_user'

    email = db.Column(db.String(50), primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.String(32), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    graduate_type = db.Column(db.Enum(GraduateChoice), nullable=False, default=GraduateChoice.WILL)

    # one to one
    apply_status = relationship("ApplyStatusModel", uselist=False, backref="user")
    info = relationship("InfoModel", uselist=False, backref="user")
    graduate_info = relationship("GraduateInfoModel", uselist=False, backref="user")
    graduate_grade = relationship("GraduateGradeModel", uselist=False, backref="user")
    ged_grade = relationship("GedGradeModel", uselist=False, backref="user")

    interview_final = relationship("InterviewFinalModel", uselist=False, backref="user")

    # one to many
    grade_info = relationship("GradeInfoModel")
    interview_data = relationship("InterviewData")


class ApplyStatusModel(db.Model):
    __tablename__ = 'apply_status'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    final_submit = db.Column(db.Boolean, nullable=False, default=False)
    pass_status = db.Column(db.Boolean, nullable=False, default=False)
    payment = db.Column(db.Boolean, nullable=False, default=False)
    receipt = db.Column(db.Boolean, nullable=False, default=False)
