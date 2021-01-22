from functools import wraps
from config.settings import KEY
from flask import request, jsonify
from datetime import datetime
import jwt
from config.status_code import TOKEN_EXPIRE, INVALID_TOKEN


def jwt_auth(auth, alg='HS256'):
    try:
        decode_auth = jwt.decode(auth, KEY, alg)
        exp = datetime.utcfromtimestamp(decode_auth['exp'])
        admin = decode_auth['role']
        if (exp - datetime.now()).total_seconds() > 0:
            return 200, True, decode_auth['user_id'], admin
    except jwt.exceptions.ExpiredSignatureError:
        return TOKEN_EXPIRE, False, None, False  # token过期
    except:
        return INVALID_TOKEN, False, None, False
    else:
        return INVALID_TOKEN, False, None, False  # 非法的token


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')
        status, auth_s, user_id, role_enum = jwt_auth(auth.encode())
        if status == 200 and auth_s and role:
            return func(*args, **kwargs)
        else:
            return jsonify({'msg': 'fail', 'status': status}), status
    return wrapper


def get_userId(request):
    auth = request.headers.get('Authorization')
    _, _, user_id, _ = jwt_auth(auth.encode())
    return user_id
