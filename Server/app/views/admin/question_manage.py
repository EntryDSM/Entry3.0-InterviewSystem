from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, admin_required

from app.models.question import Question
from app.models import db

api = Api(Blueprint('question', __name__))
api.prefix = '/admin/manage'


@api.resource('/')
class QuestionList(BaseResource):
    @admin_required
    def get(self):
        questions = Question.query.all()

        return [dict(question) for question in questions], 200


