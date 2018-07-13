from app import create_app
from app.models import db
from config.dev import Config
from app.models.admin import Admin, AdminTypeEnum
from app.models.info import Info
from werkzeug.security import generate_password_hash
import unittest
import json

app = create_app(Config)


class BaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        app.testing = True
        self.tester = app.test_client(self)

    def _get_tokens(self):
        response = self.tester.post('/auth',
                                    data=json.dumps(dict(
                                                    username="admin",
                                                    password="admin1234"
                                                    )),
                                    content_type='application/json')

        response = json.loads(response.data.decode())

        self.admin_access_token = response['access_token']
        self.admin_refresh_token = response['refresh_token']

        response = self.tester.post('/auth',
                                    data=json.dumps(dict(
                                                    username="interview",
                                                    password="admin1234"
                                                    )),
                                    content_type='application/json')

        response = json.loads(response.data.decode())

        self.interview_access_token = response['access_token']
        self.interview_refresh_token = response['refresh_token']

    def _create_fake_admin(self):
        admin = Admin(email="admin@entrydsm.hs.kr",
                      password=generate_password_hash("admin1234"),
                      admin_type=AdminTypeEnum.ROOT,
                       name="에리히")

        interviewer = Admin(email="interview@entrydsm.hs.kr",
                            password=generate_password_hash("admin1234"),
                            admin_type=AdminTypeEnum.INTERVIEW,
                            name="루델")

        db.session.add(admin)
        db.session.add(interviewer)

        db.session.commit()

    def _create_fake_apply(self):
        apply = Info(user_id="",
                     address_base="서울시 종로구 세종대로 172",
                     address_detail="광화문",
                     name="루벤도르프",
                     parent_name="롬멜",
                     parent_tell="01012345678",
                     introduce="자기소개",
                     study_plan="학업계획서",
                     exam_code="123456")

        db.session.add(apply)

        db.session.commit()

    def setUp(self):
        self._create_fake_admin()
        self._create_fake_apply()
        self._get_tokens()

    def tearDown(self):
        Admin.query.delete()

    def request(self, method, target_uri, data=None, token=None, user_type="admin"):
        if token is None:
            if user_type == "admin":
                token = self.admin_access_token
            elif user_type == "interview":
                token = self.interview_access_token
            else:
                raise RuntimeError("Unexpected user type {0} given".format(user_type))

        return method(target_uri,
                      data=json.dumps(data),
                      headers={"Authorization": "Bearer {}".format(token)},
                      content_type='application/json'
                      )
