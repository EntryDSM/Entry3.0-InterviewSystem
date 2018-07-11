from flask import (Blueprint, request, abort)
from flask_restful import Api
from app.views import BaseResource, auth_required, get_jwt_identity
from app.models import db
from app.models.interview_data import InterviewData
from app.models.info import Info
from app.models.question import Question
from app.models.admin import Admin

api = Api(Blueprint('grading', __name__))


@api.resource('/<int: exam_code>/<int: question_id>')
class Grading(BaseResource):
    @auth_required
    def post(self, exam_code: int, question_id: int):
        request_data = request.json

        take_interview = request_data["take_interview"]
        grading = request_data["grading"]
        comment = request_data["comment"] if request_data["comment"] else ""

        admin = get_jwt_identity()
        admin = Admin.query.filter_by(email=admin).first()

        info = Info.query.filter_by(exam_code=exam_code).first()
        question = Question.query.filter_by(question_id=question_id).first()

        # question matching check
        original_question = list(question.values())
        requested_question = list(grading.keys())
        if original_question != requested_question:
            abort(400)

        new_interview_data = InterviewData(info_id=info.info_id,
                                           admin_id=admin.admin_id,
                                           question_id=question.question_id,
                                           take_interview=take_interview,
                                           interview_result=grading,
                                           comment=comment,)

        db.session.commit(new_interview_data)
        db.session.add()

        return 200

