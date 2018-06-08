from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class GradeInfo(db.Model):
    __tablename__ = "grade_info"

    is_pass = db.Column('pass', db.Boolean)
    score = db.Column(db.CHAR)
    subject = db.Column(db.VARCHAR)
    grade = db.Column(Integer(unsigned=True))
    semester = db.Column(Integer(unsigned=True))