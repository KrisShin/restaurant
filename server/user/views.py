from flask import Blueprint, jsonify, request
from .models import User
from utils.util import make_password

user = Blueprint('User', __name__, url_prefix='/user')

@user.route('/test',methods=['POST','GET'])
def test():

    data = request.json
    nickname = data.get('nickname')
    phone = data.get('phone')
    password = make_password(data.get('password'))
    age = data.get('age')
    avatar = data.get('avatar')
    user = User(na)

    return jsonify({'msg':'OK'})