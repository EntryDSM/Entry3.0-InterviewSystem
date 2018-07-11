from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, auth_required

from app.models.question import Question
from app.models import db

api = Api(Blueprint('question', __name__))
api.prefix = '/admin'


@api.resource('/new')
class Maker(BaseResource):
    @auth_required
    def post(self):
        request_data = request.json

        title = request_data["title"]
        body = request_data["body"]
        form = request_data["form"]

        new_question = Question(title=title, body=body, form=form)
        db.session.add(new_question)
        db.session.commit()

        return 200
