from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, admin_required

from app.models.question import Question
from app.models import db

api = Api(Blueprint('question', __name__))
api.prefix = '/admin/question'


@api.resource('/')
class QuestionList(BaseResource):
    @admin_required
    def get(self):
        questions = Question.query.all()

        return [dict(question) for question in questions], 200


@api.resource('/<question_id: int>')
class Manage(BaseResource):
    @admin_required
    def get(self, question_id: int):
        question = Question.query.fitler_by(question_id=question_id)

        return dict(question), 200

    @admin_required
    def post(self, question_id: int):
        request_change = request.json
        Question.query.fitler_by(question_id=question_id).update(request_change)
        db.session.commit()

        return 200

    @admin_required
    def delete(self, question_id: int):
        Question.query.fitler_by(question_id=question_id).delete()

        return 200
