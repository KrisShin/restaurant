from flask import Blueprint, jsonify, request
# from .models import User
from utils.util import make_password
from config.global_params import  db

order = Blueprint('Order', __name__, url_prefix='/order')


# @user.route('/test', methods=['POST', 'GET'])
# def test():
#     if request.method == "GET":
#         return jsonify({'msg': 'method GET ok'})

#     if request.method == "POST":
#         data = request.get_json()
#         nickname = data.get('nickname')
#         phone = data.get('phone')
#         password = make_password(data.get('password'))
#         age = data.get('age')
#         avatar = data.get('avatar')
#         user = User(nickname=nickname, phone=phone, age=age,
#                     password=password, avatar=avatar)
#         db.session.add(user)
#         db.session.commit()

#         return jsonify({'msg': 'OK'})
