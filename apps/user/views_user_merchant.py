from utils.wraps import auth, clear_login_cache, get_current_user, set_login_cache
from config.settings import KEY
from datetime import datetime, timedelta
from config import status_code
from utils.util import check_password, get_captcha, make_password
from flask import Blueprint, jsonify, request
from apps.user.models import User
from apps.order.models import Order
import jwt
from utils.mail_sender import sender
from utils.rest_redis import r

user = Blueprint('Merchant', __name__, url_prefix='/merchant/user')


@user.route('/login/', methods=['POST'])
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
    sender.send(email, mail)
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
    r.del_val(f'user_{user.id}:captcha')
    return jsonify({'code': status_code.OK, "msg": "修改密码成功, 请重新登录"})


@user.route('/reset_pwd/', methods=['PUT'])
def user_reset_pwd():
    '''user reset password'''
    data = request.get_json()
    email = data.get('email')
    captcha = data.get('captcha')
    new_passwd = data.get('new_password')
    confirm_passwd = data.get('cfm_password')

    if not all((email, captcha, new_passwd, confirm_passwd)):
        return jsonify({'code': status_code.PARAM_LACK, 'msg': '参数不全'})

    user = User.query.filter_by(email=email).first()

    if confirm_passwd != new_passwd:
        return jsonify(
            {'code': status_code.USER_WRONG_CONFIRM_PASSWORD, 'msg': '两次输入密码不同'}
        )

    if check_password(user.password, new_passwd):
        return jsonify({'code': status_code.USER_SAME_PASSWORD, 'msg': '新密码不能与旧密码相同'})

    real_captcha = r.get_val(f'user_{user.id}:captcha')
    if not real_captcha:
        return jsonify(
            {'code': status_code.USER_CAPTCHA_EXPIRED, 'msg': '验证码已过期, 请重新申请'}
        )
    if captcha != real_captcha:
        return jsonify({'code': status_code.USER_WRONG_CAPTCHA, 'msg': '验证码错误'})

    user.password = make_password(new_passwd)
    user.save()
    r.del_val(f'user_{user.id}:captcha')
    return jsonify({'code': status_code.OK, "msg": "重置密码成功"})


@user.route('/list/', methods=['GET'])
def get_customer_list():
    data = request.args
    page = int(data.get('page', 1)) or 1
    pageSize = int(data.get('pageSize', 10))
    resp = []
    users = User.query.filter(role='user')
    for user in users:
        user = dict(user)
        user.pop('balance')
        user.pop('gender')
        user.pop('is_new')
        user.pop('default_addr')
        user['phone'] = user['phone'][:3] + '*' * 4 + user['phone'][-4:]
        user['order_count'] = Order.query.filter_by(user_id=user['user_id']).count()
        resp.append(user)

    return jsonify(
        {
            'code': status_code.OK,
            "data": resp,
            'page': page,
            'pageSize': pageSize,
            'total': users.count(),
        }
    )

@user.route('/profile/', methods=['GET', 'PUT'])
@auth
def user_profile():
    '''check user profile'''
    user = get_current_user(request)
    if request.method == 'GET':
        '''Get user profile.'''
        resp = dict(user)
        return jsonify({'code': status_code.OK, 'data': resp})
    # elif request.method == 'PUT':
    #     '''Modify user.'''
    #     data = request.get_json()
    #     # Get base64 code and tranform to picture and save.
    #     base64_str = data.get('avatar')
    #     avatar_path = None
    #     if base64_str:
    #         avatar_path = save_img('avatar', base64_str)
    #     age = data.get('age')
    #     nickname = data.get('nickname')

    #     if avatar_path:
    #         del_invalify_image(user.avatar)
    #         user.avatar = avatar_path
    #     if age:
    #         user.age = age
    #     if nickname:
    #         user.nickname = nickname
    #     user.save()

    #     return jsonify(
    #         {'code': status_code.OK, 'data': {'avatar': HTTP_HOST + user.avatar}}
    #     )