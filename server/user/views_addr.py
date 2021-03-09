from flask import Blueprint, request, jsonify

from .models import User, Address
from config.status_code import ADDR_DATA_ERROR
from utils.wraps import auth, get_userId

address = Blueprint('Address', __name__, url_prefix='/addr')


@address.route('/<int:addr_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def oprate_address(addr_id):
    if request.method == 'GET':
        addr = Address.query.filter(id=addr_id).first()
        return jsonify({'success': True, 'data': dict(addr)})

    if request.method == 'POST':
        if addr_id != 0:
            return jsonify({'success': False, 'code': ADDR_DATA_ERROR})
        data = request.get_json()
        '''
        {'name': 'Goku', 'tel': '12343214123', 'country': '', 'province': '四川省', 'city': '成都市', 'county': '青羊区', 'areaCode': '510105', 'postalCode': '', 'addressDetail': 'kakagogo', 'isDefault': False, 'id': 0}
        '''
        user = User.query.filter(id=get_userId(request)).first()
        name = data.get('name')
        phone = data.get('tel')
        location = {
            'country': data.get('country'),
            'province': data.get('province'),
            'city': data.get('city'),
            'county': data.get('county'),
            'areaCode': data.get('areaCode'),
            'addressDetail': data.get('addressDetail')
        }
        is_default = data.get('isDefault')
        addr = Address(name=name, phone=phone, location=location,
                       user=user, is_default=is_default)
        return jsonify({'success': True, 'data': request.get_json()})

    if request.method == 'PUT':
        addr = Address.query.filter(id=addr_id).first()
        return jsonify({'success': True, 'data': request.get_json()})

    if request.method == 'DELETE':
        addr = Address.query.filter(id=addr_id).first()
        return jsonify({'success': True, 'data': request.get_json()})


@address.route('/addrList', methods=["GET"])
@auth
def get_addr_by_id():
    user = User.query.filter(id=get_userId(request)).first()
    addrs = [dict(addr) for addr in user.address]
    return jsonify({'success': True, 'data': {'addresses': addrs}})
