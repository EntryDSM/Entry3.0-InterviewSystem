from app.models import db
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer
from .interview_data import InterviewData


class Question(db.Model):
    __tablename__ = "question"

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60))
    body = db.Column(db.String(1023))
    form = db.Column(db.JSON)

    # one to one
    interview_data = relationship("InterviewData", uselist=False, backref="question")