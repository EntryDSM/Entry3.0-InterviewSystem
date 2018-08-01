from flask import (Blueprint, request, abort)
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, get_raw_jwt
from app.views import blacklist_check, blacklist, BaseResource
from werkzeug.security import check_password_hash
from flasgger import swag_from
from app.docs.auth.auth import *

from app.models.admin import Admin

api = Api(Blueprint('auth', __name__))


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH)
    def post(self):
        request_data = request.json
        email = request_data['email']
        password = request_data['password']

        admin = Admin.query.filter_by(email=email).first()

        if check_password_hash(admin.password, password):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)

            response = dict(
                access_token=access_token,
                refresh_token=refresh_token
            )

            return response, 200

        else:
            abort(401)


@api.resource('/refresh')
class Refresh(Resource):
    @blacklist_check
    @swag_from(REFRESH)
    def post(self):
        current_user = get_jwt_identity()
        response = dict(
            access_token=create_access_token(identity=current_user)
        )

        return response, 200


@api.resource('/logout')
class Logout(Resource):
    @swag_from(LOGOUT)
    @blacklist_check
    def delete(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)

        return 200
