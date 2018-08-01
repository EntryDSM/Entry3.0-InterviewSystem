from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, admin_required

from app.models.question import Question
from app.models.info import Info
from app.models.user import User
from app.models.graduate_info import GraduateInfo
from app.models import db

from app.docs.interview.search import SEARCH
from flasgger import swag_from

api = Api(Blueprint('search', __name__))
api.prefix = '/search'


@api.resource("/<int:exam_code>")
class Search(BaseResource):
    @admin_required
    @swag_from(SEARCH)
    def get(self, exam_code: int):
        questions = Question.query.all()
        questions = [[question.title, question.question_id] for question in questions]

        student_info = db.session.query(User, Info, GraduateInfo)\
            .join(Info)\
            .join(GraduateInfo)\
            .filter(Info.exam_code==exam_code).first()

        student_info = {
            "name": student_info.Info.name,
            "admission_type": str(student_info.Info.admission),
            "img_path": student_info.Info.img_path,
            "school": student_info.GraduateInfo.school_name
        }

        response = {
            "question_list": questions,
            "student_info": student_info
        }

        return self.unicode_safe_json_dumps(response, 200)
