from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer


class Question(db.Model):
    __tablename__ = "question"

    question_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    form = db.Column(db.JSON)
