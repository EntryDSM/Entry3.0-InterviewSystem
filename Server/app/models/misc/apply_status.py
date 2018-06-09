from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class ApplyStatus(db.Model):
    __tablename__ = "apply_status"

    info_id = db.Column(db.Integer, db.ForeignKey('info.info_id'))
    payment = db.Column(db.Boolean)
    receipt = db.Column(db.Boolean)
    final_submit = db.Column(db.Boolean)
    pass_status = db.Column(db.Boolean)
