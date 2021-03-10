import json
from server.config.status_code import ADDR_LACK_DATA

from flask import Blueprint, request, jsonify

from .models import User, Address
from config.global_params import db
from config.status_code import *
from utils.wraps import auth, get_userId

address = Blueprint('Address', __name__, url_prefix='/addr')


@address.route('/<int:addr_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def oprate_address(addr_id):
    if request.method == 'GET':
        addr = Address.query.filter_by(id=addr_id).first()
        if addr:
            return jsonify({'success': True, 'data': dict(addr)})
        else:
            return jsonify({'success': False, 'code': ADDR_NOT_EXISIT})

    if request.method == 'POST':
        if addr_id != 0:
            return jsonify({'success': False, 'code': ADDR_DATA_ERROR})
        data = request.get_json()
        user = User.query.filter_by(id=get_userId(request)).first()
        addr = Address()
        addr = operate_an_addr(addr, user, data)
        if not addr:
            return jsonify({'success': False, 'code': ADDR_LACK_DATA})
        db.session.add(addr)
        db.session.commit()
        return jsonify({'success': True})

    if request.method == 'PUT':
        if addr_id == 0:
            return jsonify({'success': False, 'code': ADDR_DATA_ERROR})
        addr = Address.query.filter_by(id=addr_id).first()
        data = request.get_json()
        user = User.query.filter_by(id=get_userId(request)).first()
        addr = operate_an_addr(addr, user, data)
        if not addr:
            return jsonify({'success': False, 'code': ADDR_LACK_DATA})
        db.session.commit()
        return jsonify({'success': True})

    if request.method == 'DELETE':
        addr = Address.query.filter_by(id=addr_id).first()
        db.session.delete(addr)
        db.session.commit()
        return jsonify({'success': True})


@address.route('/list', methods=["GET"])
@auth
def get_addr_by_id():
    user = User.query.filter_by(id=get_userId(request)).first()
    addrs = [dict(addr) for addr in user.address]
    return jsonify({'success': True, 'data': {'addresses': addrs}})


def operate_an_addr(addr, user, data):
    name = data.get('name')
    phone = data.get('tel')
    location = {
        'country': data.get('country'),
        'province': data.get('province'),
        'city': data.get('city'),
        'county': data.get('county'),
        'addressDetail': data.get('addressDetail'),
        'areaCode': data.get('areaCode')
    }

    is_default = data.get('isDefault')
    if is_default:
        for a in user.address:
            a.is_default = False
    if not all((name,phone,location,user,addr)):
        return
    addr.name = name,
    addr.phone = phone
    addr.location = location
    addr.user = user
    addr.is_default = is_default
    addr.set_update_time()
    return addr
