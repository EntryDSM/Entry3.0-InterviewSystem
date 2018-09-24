from enum import Enum

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer

from app.models import db


class AdminTypeChoice(Enum):
    ROOT = 1
    ADMINISTRATION = 2
    QNA = 3
    INTERVIEW = 4


class InterviewFinalModel(db.Model):
    __tablename__ = 'interview_final'

    # one to one
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    final_score = db.Column(Integer(unsigned=True), nullable=True)


class InterviewData(db.Model):
    __tablename__ = 'interview_data'

    # one to many => user
    # one to many => admin
    # one to one => question
    user_id = db.Column(db.String(32), db.ForeignKey('user.user_id', ondelete='CASCADE'), primary_key=True)
    admin_id = db.Column(db.String(32), db.ForeignKey('admin.admin_id', ondelete='CASCADE'), primary_key=True)
    question_id = db.Column(Integer(unsigned=True), db.ForeignKey('question.question_id', ondelete='CASCADE'),
                            primary_key=True)
    comment = db.Column(db.String(255), nullable=True)
    interview_result = db.Column(db.JSON, nullable=True)
    take_interview = db.Column(db.Boolean, nullable=True, default=True)


class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(Integer(unsigned=True), primary_key=True)
    body = db.Column(db.String(1023), nullable=True)
    form = db.Column(db.JSON, nullable=True)
    title = db.Column(db.String(60), nullable=True)

    # one to one
    interview_data = relationship("InterviewData", uselist=False, backref="question")


class AdminModel(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    admin_type = db.Column(db.Enum(AdminTypeChoice), nullable=False, default=AdminTypeChoice.INTERVIEW)
    email = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(200), nullable=True)

    # one to many
    interview_data = relationship("InterviewData")
