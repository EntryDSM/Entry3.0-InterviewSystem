from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class GradudateInfo(db.Model):
    __tablename__ = "graduate_info"

    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id", ondelete='CASCADE'), primary_key=True)
    graduate_year = db.Column(Integer(unsigned=True), nullable=False, default=2019)
    school_code = db.Column(db.String(32), nullable=False, default="")
    school_name = db.Column(db.String(50), nullable=False, default="")
    student_number = db.Column(db.String(5), nullable=False, default="")
