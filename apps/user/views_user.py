from datetime import datetime, timedelta
import jwt
import re

from flask import Blueprint, jsonify, request

from .models import User, Account
from config import status_code
from config.settings import KEY, HTTP_HOST
from apps.dish.models import Tag
from utils.mail_sender import sender
from utils.rest_redis import r
from utils.util import (
    make_password,
    check_password,
    get_captcha,
    save_img,
    del_invalify_image,
)
from utils.wraps import auth, clear_login_cache, get_current_user, set_login_cache

user = Blueprint('User', __name__, url_prefix='/customer/user')


@user.route('/register/', methods=['POST'])
def user_register():
    '''register a new user.'''
    data = request.get_json()
    nickname = data.get('nickname')
    phone = data.get('phone')
    gender = bool(data.get('gender'))
    age = data.get('age')
    email = data.get('email')
    password = make_password(data.get('password'))

    # check phone number
    reg_phone = r'^1[3-9]\d{9}$'
    if not re.match(reg_phone, phone):
        return jsonify({'code': status_code.USER_WRONG_PHONE_FORMAT, 'msg': '手机号格式错误'})

    user = User.query.filter_by(phone=phone).first()
    if user:
        return jsonify({'code': status_code.USER_EXISTED, 'msg': '手机号已注册'})

    user = User(
        nickname=nickname,
        phone=phone,
        age=age,
        email=email,
        password=password,
        gender=gender,
        avatar='/static/avatar/default.jpg',
    )
    account = Account(user=user)
    user.save()
    account.save()

    return jsonify({'code': status_code.OK})


@user.route('/login/', methods=['POST'])
def user_login():
    '''Login user by phone and password.'''

    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    user = User.query.filter_by(phone=phone).first()
    if not user:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '用户不存在'})

    if not check_password(user.password, password):
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '密码错误'})

    Authorization = jwt.encode(
        {
            'user_id': user.id,
            'exp': datetime.now() + timedelta(hours=2),
            'role': user.role,
        },
        KEY,
        'HS256',
    )

    set_login_cache(Authorization, user.id)

    return jsonify({"code": status_code.OK, 'token': Authorization})


@user.route('/email_captcha/', methods=['POST'])
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


@user.route('/change_pwd/', methods=['PUT'])
@auth
def user_change_pwd():
    '''user change password'''
    data = request.get_json()
    email = data.get('email')
    captcha = data.get('captcha')
    old_passwd = data.get('old_password')
    new_passwd = data.get('new_password')
    confirm_passwd = data.get('cfm_password')
    user = get_current_user(request)

    if email != user.email:
        return jsonify({'code': status_code.USER_WRONG_EMAIL, 'msg': '请输入本人邮箱'})

    if confirm_passwd != new_passwd:
        return jsonify(
            {'code': status_code.USER_WRONG_CONFIRM_PASSWORD, 'msg': '两次输入密码不同'}
        )

    if old_passwd == new_passwd:
        return jsonify({'code': status_code.USER_SAME_PASSWORD, 'msg': '新密码不能与旧密码相同'})

    real_captcha = r.get_val(f'user_{user.id}:captcha')
    if not real_captcha:
        return jsonify(
            {'code': status_code.USER_CAPTCHA_EXPIRED, 'msg': '验证码已过期, 请重新申请'}
        )
    if captcha != real_captcha:
        return jsonify({'code': status_code.USER_WRONG_CAPTCHA, 'msg': '验证码错误'})

    if not check_password(user.password, old_passwd):
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '原密码错误'})

    user.password = make_password(new_passwd)
    user.save()
    clear_login_cache()
    return jsonify({'code': status_code.OK, "msg": "修改密码成功, 请重新登录"})


@user.route('/profile/', methods=['GET', 'PUT'])
@auth
def user_profile():
    '''check user profile'''
    user = get_current_user(request)
    if request.method == 'GET':
        '''Get user profile.'''
        resp = dict(user)
        return jsonify({'code': status_code.OK, 'data': resp})
    elif request.method == 'PUT':
        '''Modify user.'''
        data = request.get_json()
        # Get base64 code and tranform to picture and save.
        base64_str = data.get('avatar')
        avatar_path = None
        if base64_str:
            avatar_path = save_img('avatar', base64_str)
        age = data.get('age')
        nickname = data.get('nickname')

        if avatar_path:
            del_invalify_image(user.avatar)
            user.avatar = avatar_path
        if age:
            user.age = age
        if nickname:
            user.nickname = nickname
        user.save()

        return jsonify(
            {'code': status_code.OK, 'data': {'avatar': HTTP_HOST + user.avatar}}
        )


@user.route('/change_email/', methods=['PUT'])
@auth
def user_edit_email():
    '''Change user's email'''
    data = request.get_json()
    email = data.get('email')
    captcha = data.get('captcha')
    user = get_current_user(request)
    # TODO: adbstract authorize captcha in a isolation function.
    real_cap = r.get_val(f'user_{user.id}:captcha')
    if not real_cap:
        return jsonify(
            {'code': status_code.USER_CAPTCHA_EXPIRED, 'msg': '验证码已过期, 请重新申请'}
        )
    if (not captcha) or (captcha != real_cap):
        return jsonify({'code': status_code.USER_WRONG_CAPTCHA, 'msg': '验证码错误'})

    ex_user = User.query.filter(User.email == email, User.id != user.id).first()
    if ex_user:
        return jsonify({'code': status_code.USER_EXISTED, 'msg': '邮箱已注册'})

    user.email = email
    if not user.is_email_active:
        user.is_email_active = True
    user.save()
    return jsonify({'code': status_code.OK})


@user.route('/logout/', methods=['POST'])
@auth
def user_logout():
    '''User logout.'''
    clear_login_cache(request)
    return jsonify({'code': status_code.OK})


@user.route('/tags/', methods=['PUT'])
@auth
def tags():
    if request.method == 'PUT':
        '''User add tag.'''
        data = request.get_json()
        user = get_current_user(request)
        exist_tags = data.get('ex_tags')

        tags = Tag.query.filter(Tag.id.in_(exist_tags)).all()
        user.tags = tags
        user.save()
        Tag.update_weight()
        return jsonify({'code': status_code.OK})


@user.route('/test/', methods=['POST', 'GET', 'PUT', 'DELETE'])
# @auth
def test():
    # mail = {
    #     'subject': f'恰了木有验证码',
    #     'content': f'<div>测试啊你个**</div>'}
    # sender.send('krisshin@88.com', mail)
    # return jsonify({'msg': 'ok'})
    # data = request.get_json()
    if request.method == "GET":
        # user = User.query.filter_by(id=1).first()
        # print(user.age, current_user.age)
        user = User.query.filter_by(id=1).first()
        # user.password = make_password("admin123")
        # db.session.commit()
        return jsonify({'msg': 'method GET ok'})

    if request.method == "POST":
        # data = request.get_json()
        # nickname = data.get('nickname')
        # phone = data.get('phone')
        # gender = data.get('gender')
        # password = make_password(data.get('password'))
        # age = data.get('age')
        # user = User(nickname=nickname, phone=phone, age=age,
        #             password=password, gender=gender, avatar='/static/avatar/default.jpg')
        # db.session.add(user)
        # db.session.commit()

        return jsonify({'msg': 'method POST OK'})
    if request.method == "PUT":
        # user = User.query.filter_by(id=1).first()
        # print(user.age, current_user.age)
        return jsonify({'msg': 'method PUT ok'})
    if request.method == "DELETE":
        # user = User.query.filter_by(id=1).first()
        # print(user.age, current_user.age)
        return jsonify({'msg': 'method DELETE ok'})
