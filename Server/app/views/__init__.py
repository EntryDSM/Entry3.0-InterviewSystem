from functools import wraps
from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import UUID
import ujson
from flask_restful import Resource
from flask import abort, current_app, g, Response
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_required, jwt_refresh_token_required

from app.models.admin import Admin


blacklist = set()


def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'
    response.headers['X-Powered-by'] = ''
    response.headers['Server'] = ''

    return response


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        account = Admin.query.filter_by(em=get_jwt_identity()).first()

        if account is None:
            abort(403)

        g.user = account.email

        return fn(*args, **kwargs)

    return wrapper


def blacklist_check(fn):
    @wraps(fn)
    @jwt_refresh_token_required
    def wrapper(*args, **kwargs):
        is_blacklisted = get_raw_jwt()['jti'] in blacklist

        if is_blacklisted:
            abort(403)

        return fn(*args, **kwargs)
    return wrapper


class BaseResource(Resource):

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs):
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8',
            **kwargs
        )

    @classmethod
    def encrypt_password(cls, password):
        return hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')

class Router:
    def __init__(self, app):
        from app.views.auth import auth
        app.register_blueprint(auth.api.blueprint)

        from app.views.admin import question_generation, question_manage
        app.register_blueprint(question_generation.api.blueprint)
        app.register_blueprint(question_manage.api.blueprint)

        from app.views.interview.grading import grading
        from app.views.interview.search import search
        app.register_blueprint(grading.api.blueprint)
        app.register_blueprint(search.api.blueprint)

        print("[INFO] Router initialized")
