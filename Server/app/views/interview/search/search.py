from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, admin_required

from app.models.question import Question
from app.models.info import Info
from app.models import db

api = Api(Blueprint('search', __name__))
api.prefix = '/search'


@api.resource("/<int:exam_code>")
class Search(BaseResource):
    @admin_required
    def get(self, exam_code: int):
        questions = Question.query.all()
        questions = [question.question_id for question in questions]

        student_info = Info.query.filter_by(exam_code=exam_code)
        student_info = {
            "name": student_info.name,
            "admission_type": str(student_info.admission),
            "img_path": student_info.img_path
        }

        response = {
            "question_list": questions,
            "student_info": student_info
        }

        return response, 200
