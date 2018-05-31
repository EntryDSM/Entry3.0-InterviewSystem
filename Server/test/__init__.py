from app import create_app
from config.dev import Config
import unittest
import json

app = create_app(Config)


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

        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']

    def setUp(self):
        self._get_tokens()

    def tearDown(self):
        pass

    def request(self, method, target_uri, data=None, token=None):
        if token is None:
            token = self.access_token

        return method(target_uri,
                      data=json.dumps(data),
                      headers={"Authorization": "Bearer {}".format(token)},
                      content_type='application/json'
                      )
