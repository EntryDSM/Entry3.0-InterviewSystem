from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class InterviewFinal(db.Model):
    __tablename__ = "interview_final"

    interview_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'), nullable=True)
    final_score = db.Column(db.Integer, nullable=True)
