from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class Interview(db.Model):
    __tablename__ = "interview_data"

    interview_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'))
    final_score = db.Column(db.Integer)

