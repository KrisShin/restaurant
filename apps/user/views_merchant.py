from utils.wraps import set_login_cache
from config.settings import KEY
from datetime import datetime, timedelta
from config import status_code
from utils.util import check_password, get_captcha, make_password
from flask import Blueprint, jsonify, request
from apps.user.models import User
import jwt
from utils.mail_sender import sender
from utils.rest_redis import r

merchant = Blueprint('Merchant', __name__, url_prefix='/merchant/user')


@merchant.route('/login/', methods=['POST'])
def login():
    '''
    Function: Merchant login view.
    '''
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    user = User.query.filter_by(phone=phone, role='admin').first()
    if not user:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '用户不存在'})

    if user.role != 'admin':
        return jsonify({'code': status_code.USER_NOT_ADMIN, 'msg': '用户不是管理员'})

    if not check_password(user.password, password):
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '密码错误'})
    # user.password = make_password(password)
    # user.save()

    # Use Key and JWT encode the user infomation to generate a token
    Authorization = jwt.encode(
        {
            'user_id': user.id,
            'exp': datetime.now() + timedelta(hours=2),
            'role': user.role,
        },
        KEY,
        'HS256',
    )

    # Set the token in Cache to sign this user already logined.
    set_login_cache(Authorization, user.id)

    return jsonify({'code': status_code.OK, "info": "", 'token': Authorization})


@merchant.route('/email_captcha/', methods=['POST'])
def send_captcha_email():
    '''
    Send captcha email to user.
    '''
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'code': status_code.PARAM_LACK, 'msg': '缺少参数'})
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '用户不存在'})

    if r.get_val(f'user_{user.id}:captcha'):
        return jsonify(
            {'code': status_code.USER_CAPTCHA_SENDED, 'msg': '验证码已发送, 请10分钟之后重试'}
        )

    captcha = get_captcha()
    print(captcha)
    mail = {
        'subject': f'恰了木有验证码',
        'content': f'''
        <div>感谢您使用恰了木有APP, 您的验证码为</div>
        <span style="font-size: 30px;font-weight: 600;background: #313131;color: #6dc4ff;">{captcha}</span>
        <div>请在10分钟之内完成验证</div>''',
    }
    r.set_val(f'user_{user.id}:captcha', captcha, 600)
    # sender.send(email, mail)
    return jsonify({'code': status_code.OK})


# @merchant.route('/list/', methods=['GET'])
def get_customer_list():
    data = [dict(user).remove() for user in User.query.filter(role='user')]
    return jsonify({'code': status_code.OK, "info": "", "data": data})
