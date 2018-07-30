from flask import (Blueprint, request)
from flask_restful import Api
from app.views import BaseResource, admin_required

from app.models.info import Info

api = Api(Blueprint('study plan', __name__))
api.prefix = '/search'


@api.resource('/<int:exam_code>/plan')
class StudyPlan(BaseResource):
    @admin_required
    def get(self, exam_code):
        study_plan = Info.query.filter_by(exam_code=exam_code).first().study_plan

        return self.unicode_safe_json_dumps(study_plan, 200)
