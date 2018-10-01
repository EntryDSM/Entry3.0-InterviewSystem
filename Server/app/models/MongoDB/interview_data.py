from mongoengine import *


class Question(Document):
    title = StringField()  # exam, plan, passion, understand, possibility, lang_use, algorithm, creativity
    body = StringField()
    judges = ListField(StringField)


class InterviewData(DynamicEmbeddedDocument):
    question = ReferenceField(Question)


class StudentData(Document):
    exam_code = StringField(primary_key=True)
    plan_test = DictField()
    passion_test = DictField()
    understand_test = DictField()
    possibility_test = DictField()

    full_score = FloatField()
    conversion_score = FloatField()

    is_take = BooleanField(default=False)


class CodeTestData(Document):
    exam_code = StringField(primary_key=True)
    lang_use = DictField()
    algorithm = DictField()
    creativity = DictField()

    score = FloatField()

    is_take = BooleanField(default=True)
