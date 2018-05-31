from functools import wraps

from flask import abort
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_required, jwt_refresh_token_required

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
        # account = AccountModel.objects(username=get_jwt_identity()).first()
        #
        # if not account:
        #     abort(403)

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


class Router:
    def __init__(self, app):
        from app.views.auth import auth
        app.register_blueprint(auth.api.blueprint)
