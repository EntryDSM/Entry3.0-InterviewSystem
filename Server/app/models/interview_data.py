from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewData(db.Model):
    __tablename__ = "interview_data"

    index = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.interview_id"))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    take_interview = db.Column(db.Boolean)
    interview_result = db.Column(db.JSON)
    grade = db.Column(db.ARRAY(db.Integer))
    comment = db.Column(db.VARCHAR(10))