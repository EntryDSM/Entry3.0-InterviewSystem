from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewData(db.Model):
    __tablename__ = "interview_data"

    interview_data_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(Integer(unsigned=True), db.ForeignKey("info.info_id"))
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.interview_id"))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    take_interview = db.Column(db.Boolean, default=True)
    interview_result = db.Column(db.JSON)
    comment = db.Column(db.VARCHAR(10))
