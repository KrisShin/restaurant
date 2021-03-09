from flask import Blueprint, request, jsonify

from .models import User
from utils.wraps import auth, get_userId

address = Blueprint('Address', __name__, url_prefix='/addr')


@address.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def oprate_address():
    if request.method == 'GET':
        user = User.query.filter(id=get_userId(request)).first()
        addrs = [dict(addr) for addr in user.address]
        return jsonify({'success': True, 'data': {'addresses': addrs}})
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
        return jsonify({'success':True, 'data': request.get_json()})
