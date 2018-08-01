from flask import request, Blueprint, Response
from flask_restful import Api
from flasgger import swag_from

from app.models import db
from app.models.question import Question
from app.views import BaseResource, admin_required

from app.docs.admin.question import *

api = Api(Blueprint('question', __name__))
api.prefix = '/admin/question'


@api.resource('/new')
class Maker(BaseResource):
    @swag_from(NEW_POST)
    @admin_required
    def post(self):
        request_data = request.json

        title = request_data["title"]
        body = request_data["body"]
        form = request_data["form"]

        new_question = Question(title=title, body=body, form=form)
        db.session.add(new_question)
        db.session.commit()

        return Response(status=200)


@api.resource('/')
class QuestionList(BaseResource):
    @admin_required
    @swag_from(MAIN_GET)
    def get(self):
        questions = Question.query.all()
        response = [question.__dict__ for question in questions]

        for r in response:
            r.pop("_sa_instance_state")

        return self.unicode_safe_json_dumps(response, 200)


@api.resource('/<int:question_id>')
class Manage(BaseResource):
    @admin_required
    @swag_from(MANAGE_GET)
    def get(self, question_id: int):
        question = Question.query.fitler_by(question_id=question_id)

        response = dict(question)

        return self.unicode_safe_json_dumps(response, 200)

    @admin_required
    def post(self, question_id: int):
    @swag_from(MANAGE_PATCH)
        request_change = request.json
        Question.query.fitler_by(question_id=question_id).update(request_change)
        db.session.commit()

        return Response(status=200)

    @admin_required
    @swag_from(MANAGE_DELETE)
    def delete(self, question_id: int):
        Question.query.fitler_by(question_id=question_id).delete()

        return Response(status=200)
