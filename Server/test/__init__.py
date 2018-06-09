from app import create_app
from app.models import db
from config.dev import Config
from app.models.misc import Admin, AdminTypeEnum
import unittest
import json

app = create_app(Config, test=True)


class BasicTestCase(unittest.TestCase):

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
        admin = Admin(admin_id="admin",
                      email="admin@entrydsm.hs.kr",
                      password="admin1234",
                      admin_type=AdminTypeEnum.ROOT)

        interviewer = Admin(admin_id="interview",
                            email="interview@entrydsm.hs.kr",
                            password="admin1234",
                            admin_type=AdminTypeEnum.INTERVIEW)

        db.session.add(admin)
        db.session.add(interviewer)

        db.session.commit()

    def setUp(self):
        self._get_tokens()

    def tearDown(self):
        pass

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
