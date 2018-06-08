from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class GedGrade(db.Model):
    __tablename__ = "ged_grade"

    ged_grade_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'))
    grade = db.Column(db.Float)
