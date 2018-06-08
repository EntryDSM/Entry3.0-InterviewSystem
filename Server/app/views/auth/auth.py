from flask import (Blueprint, request, abort)
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, get_raw_jwt
from uuid import uuid4
from app.views import blacklist_check, blacklist

api = Api(Blueprint('auth', __name__))


@api.resource('/auth')
class Auth(Resource):
    def post(self):
        return 200


@api.resource('/refresh')
class Refresh(Resource):
    @blacklist_check
    def post(self):
        return 200


@api.resource('logout')
class Logout(Resource):
    @blacklist_check
    def delete(self):
        return 200
