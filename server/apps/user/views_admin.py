from utils.wraps import set_login_cache
from config.settings import KEY
from datetime import datetime, timedelta
from config.status_code import USER_NOT_ADMIN, USER_NOT_EXIST, USER_WRONG_PASSWORD
from utils.util import check_password
from flask import Blueprint, jsonify, request
from apps.user.models import User
import jwt


merchant = Blueprint(__name__, url_prefix='/admin/user')


@merchant.route('/login')
def login():
    '''
    Function: Merchant login view.
    '''
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    user = User.query.filter_by(phone=phone).first()
    if not user:
        return jsonify({'success': False, 'code': USER_NOT_EXIST})

    if user.role != 'admin':
        return jsonify({'success': False, 'code': USER_NOT_ADMIN})

    if not check_password(password, user.password):
        return jsonify({'success': False, 'code': USER_WRONG_PASSWORD})

    # Use Key and JWT encode the user infomation to generate a token
    Authorization = jwt.encode(
        {'user_id': user.id, 'exp': datetime.now() + timedelta(hours=2), 'role': user.role}, KEY, 'HS256')

    # Set the token in Cache to sign this user already logined.
    set_login_cache(Authorization, user.id)

    return jsonify({"success": True, "info": "",  'token': Authorization})
