from app.models import db


class School(db.Model):
    __tablename__ = 'school'

    name = db.Column(db.VARCHAR)
    code = db.Column(db.VARCHAR)
    goverment = db.Column(db.VARCHAR)
    school_region = db.Column(db.VARCHAR)
