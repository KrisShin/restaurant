from datetime import datetime
from functools import wraps

from flask import request, jsonify
import jwt

from config.settings import KEY
from config.status_code import TOKEN_EXPIRE, INVALID_TOKEN
from utils.rest_redis import r


def jwt_auth(auth, alg='HS256'):
    if not r.get_val(f'user:{auth}'):
        return TOKEN_EXPIRE, False, None, False  # token过期
    try:
        decode_auth = jwt.decode(auth, KEY, alg)
        exp = datetime.utcfromtimestamp(decode_auth['exp'])
        admin = decode_auth['role']
        if (exp - datetime.now()).total_seconds() > 0:
            return 200, True, decode_auth['user_id'], admin
    except jwt.exceptions.ExpiredSignatureError:
        return TOKEN_EXPIRE, False, None, False  # token过期
    except Exception as e:
        print(e)
        return INVALID_TOKEN, False, None, False
    else:
        return INVALID_TOKEN, False, None, False  # 非法的token


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')
        status, auth_s, _, role = jwt_auth(auth.encode())
        if status == 200 and auth_s and role:
            return func(*args, **kwargs)
        else:
            return jsonify({'success': False, 'status': status}), status
    return wrapper


def set_login_cache(req):
    r.set_val(f'user:{req.headers.get("Authorization")}', 7200)


def clear_login_cache(req):
    r.del_val(f'user:{req.headers.get("Authorization")}')


def get_userId(req):
    return r.get_val(f'user:{req.headers.get("Authorization")}')
