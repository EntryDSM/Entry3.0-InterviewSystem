from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class GraduateGrade(db.Model):
    __tablename__ = "graduate_grade"

    grade_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'))
    volunteer_time = db.Column(Integer(unsigned=True))
    final_score = db.Column(db.Float)
