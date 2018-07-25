from flask import (Blueprint, request, abort)
from flask_restful import Api
from app.views import BaseResource, auth_required, get_jwt_identity
from app.models import db
from app.models.interview_data import InterviewData
from app.models.info import Info
from app.models.question import Question
from app.models.admin import Admin
from app.models.user import User

api = Api(Blueprint('grading', __name__))


@api.resource('/<exam_code>/<question_id>')
class Grading(BaseResource):
    @auth_required
    def post(self, exam_code: str, question_id: int):
        request_data = request.json

        take_interview = request_data["take_interview"]
        grading = request_data["grading"]
        comment = request_data["comment"]

        admin = get_jwt_identity()
        admin = Admin.query.filter_by(email=admin).first()

        info = Info.query.filter_by(exam_code=exam_code).first()
        user = User.query.filter_by(user_id=info.user_id).first()
        question = Question.query.filter_by(question_id=question_id).first()

        # question matching check
        original_question = list(question.form.values())
        requested_question = list(grading.keys())

        if original_question != requested_question:
            abort(400)

        new_interview_data = InterviewData(user_id=user.user_id,
                                           admin_id=admin.admin_id,
                                           question_id=question.question_id,
                                           take_interview=take_interview,
                                           interview_result=grading,
                                           comment=comment)

        db.session.add(new_interview_data)
        db.session.commit()

        return 200

    @auth_required
    def get(self, exam_code: int, question_id: int):
        question = Question.query.filter_by(question_id=question_id).first()
        question = question.__dict__
        question.pop("_sa_instance_state")

        return self.unicode_safe_json_dumps(question, 200)
