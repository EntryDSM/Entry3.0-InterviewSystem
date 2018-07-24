from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewFinal(db.Model):
    __tablename__ = "interview_final"

    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id", ondelete='CASCADE'), primary_key=True)
    final_score = db.Column(Integer(unsigned=True), nullable=True)
