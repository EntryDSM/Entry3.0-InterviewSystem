from enum import Enum

from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.dialects.mysql import DOUBLE as Double
from sqlalchemy import PrimaryKeyConstraint

from app.models import db


class ScoreChoice(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6


class SubjectChoice(Enum):
    KOREAN = 1
    MATHEMATICS = 2
    SOCIAL = 3
    HISTORY = 4
    SCIENCE = 5
    TECH = 6
    ENGLISH = 7


class GraduateInfoModel(db.Model):
    __tablename__ = 'graduate_info'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    graduate_year = db.Column(Integer(unsigned=True), nullable=False, default=2019)
    school_code = db.Column(db.String(32), nullable=False, default="")
    school_name = db.Column(db.String(50), nullable=False, default="")
    student_number = db.Column(db.String(5), nullable=False, default="")


class GraduateGradeModel(db.Model):
    __tablename__ = 'graduate_grade'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    first_grade = db.Column(Double(), nullable=False, default=0.0)
    second_grade = db.Column(Double(), nullable=False, default=0.0)
    third_grade = db.Column(Double(), nullable=False, default=0.0)
    conversion_score = db.Column(Double(), nullable=False, default=0.0)
    attendance_score = db.Column(Integer(unsigned=True), nullable=False, default=0)
    volunteer_score = db.Column(Double(), nullable=False, default=0.0)
    final_score = db.Column(Double(), nullable=False, default=0.0)
    volunteer_time = db.Column(Integer(unsigned=True), nullable=False, default=0)
    period_cut = db.Column(Integer(unsigned=True), nullable=False, default=0)
    full_cut = db.Column(Integer(unsigned=True), nullable=False, default=0)
    late = db.Column(Integer(unsigned=True), nullable=False, default=0)
    early_leave = db.Column(Integer(unsigned=True), nullable=False, default=0)


class GradeInfoModel(db.Model):
    __tablename__ = 'grade_info'

    # one to many
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    is_pass = db.Column(db.Boolean, nullable=False, default=True)
    score = db.Column(db.Enum(ScoreChoice), nullable=True)
    semester = db.Column(Integer(), primary_key=True)
    subject = db.Column(db.Enum(SubjectChoice), primary_key=True)

    # __table_args__ = (
    #     PrimaryKeyConstraint('user_id', 'semester'),
    #     {},
    # )


class GedGradeModel(db.Model):
    __tablename__ = 'ged_grade'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    grade = db.Column(Double(), nullable=False)
    conversion_score = db.Column(Double(), nullable=False, default=0.0)
    attendance_score = db.Column(Integer(unsigned=True), nullable=False, default=15)
    volunteer_score = db.Column(Double(), nullable=False, default=0.0)
    final_score = db.Column(Double(), nullable=False, default=0.0)
