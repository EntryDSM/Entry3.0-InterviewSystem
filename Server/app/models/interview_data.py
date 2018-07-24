from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewData(db.Model):
    __tablename__ = "interview_data"

    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id", ondelete='CASCADE'), primary_key=True)
    admin_id = db.Column(db.String(32), db.ForeignKey('admin.admin_id', ondelete='CASCADE'), primary_key=True)
    question_id = db.Column(Integer(unsigned=True), db.ForeignKey('question.question_id', ondelete='CASCADE'), primary_key=True)
    take_interview = db.Column(db.Boolean, default=True)
    interview_result = db.Column(db.JSON)
    comment = db.Column(db.String(255))
