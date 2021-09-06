from datetime import datetime
from functools import wraps

from flask import request, jsonify
import jwt

from config.settings import KEY
from config.status_code import USER_TOKEN_EXPIRE, USER_INVALID_TOKEN
from utils.rest_redis import r


def jwt_auth(auth, alg='HS256'):
    '''JWT encoding to authorization user.'''
    if not r.get_val(f'user:{auth.decode()}'):
        print(auth.decode())
        return USER_TOKEN_EXPIRE, False, None, False  # token过期
    try:
        decode_auth = jwt.decode(auth, KEY, alg)
        exp = datetime.utcfromtimestamp(decode_auth['exp'])
        admin = decode_auth['role']
        if (exp - datetime.now()).total_seconds() > 0:
            return 200, True, decode_auth['user_id'], admin
    except jwt.exceptions.ExpiredSignatureError:
        return USER_TOKEN_EXPIRE, False, None, False  # token过期
    except Exception as e:
        print(e)
        return USER_INVALID_TOKEN, False, None, False
    else:
        return USER_INVALID_TOKEN, False, None, False  # 非法的token


def auth(func):
    '''Authorization is user logined.'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')
        status, auth_s, _, role = jwt_auth(auth.encode())
        if status == 200 and auth_s and role:
            return func(*args, **kwargs)
        else:
            return jsonify({'success': False, 'code': status})  # , status

    return wrapper


def set_login_cache(auth, user_id):
    '''Set user logined cache. And cache will delete in one hour.'''
    print(auth)
    r.set_val(f'user:{auth}', user_id, 3600 * 1)


def clear_login_cache(req):
    '''Manually delete the user logined cache.'''
    r.del_val(f'user:{req.headers.get("Authorization")}')


def get_userId(req):
    '''Get current logined user's ID from cache'''
    return r.get_val(f'user:{req.headers.get("Authorization")}')
