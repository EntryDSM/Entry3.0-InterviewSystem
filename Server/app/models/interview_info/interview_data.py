from app.models import db


class InterviewData(db.Model):
    __tablename__ = "interview_result"

    interview_id = db.Column(db.Integer, db.ForeignKey("interview.interview_id"))
    question_id = db.Column(db.Integer, db.ForeignKey('interview_question.question_id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    take_interview = db.Column(db.Boolean)
    grade = db.Column(db.ARRAY(db.Integer))
    comment = db.Column(db.VARCHAR)
