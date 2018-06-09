from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewQuestion(db.Model):
    __tablename__ = "interview_question"

    question_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    title = db.Column(db.VARCHAR)
    body = db.Column(db.VARCHAR)
    subject_list = db.Column(db.ARRAY(db.String))
