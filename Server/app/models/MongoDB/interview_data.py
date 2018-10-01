from mongoengine import *


class StudentData(Document):
    exam_code = StringField(primary_key=True)
    plan_test = DictField()
    passion_test = DictField()
    understand_test = DictField()
    possibility_test = DictField()

    interview_score = FloatField()
    conversion_score = FloatField()

    is_take = BooleanField(default=False)


class CodeTestData(Document):
    exam_code = StringField(primary_key=True)
    lang_use = DictField()
    algorithm = DictField()
    creativity = DictField()

    code_score = FloatField()

    is_take = BooleanField(default=True)


