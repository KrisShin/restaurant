from flask import Blueprint, request, jsonify

from .models import User, Address
from config.global_params import db
from config.status_code import *
from utils.wraps import auth, get_userId

address = Blueprint('Address', __name__, url_prefix='/customer/addr')


@address.route('/<int:addr_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def oprate_address(addr_id):
    '''All operation of address'''
    if request.method == 'GET':
        '''Get an addres.'''
        addr = Address.query.filter_by(id=addr_id).first()
        if addr:
            return jsonify({'success': True, 'data': dict(addr)})
        else:
            return jsonify({'success': False, 'code': ADDR_NOT_EXISIT})

    if request.method == 'POST':
        '''Create an address'''
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
        '''Modify infomation of address'''
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
        '''Delete the address'''
        addr = Address.query.filter_by(id=addr_id).first()
        addr.delete()
        db.session.commit()
        return jsonify({'success': True})


@address.route('/list', methods=["GET"])
@auth
def get_addr_by_id():
    '''All address list.'''
    user = User.query.filter_by(id=get_userId(request)).first()
    addrs = [dict(addr) for addr in user.address]
    return jsonify({'success': True, 'data': {'addresses': addrs}})


def operate_an_addr(addr, user, data):
    '''Set address properties.'''
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
    # if this address was set as default, other address unset default.
    if user.address:
        if is_default:
            for a in user.address:
                a.is_default = False
    else:
        is_default = True
    if not all((name, phone, location, user, addr)):
        return
    addr.name = name,
    addr.phone = phone
    addr.location = location
    addr.user = user
    addr.is_default = is_default
    addr.set_update_time()
    return addr

# @address.route('/getDefault', methods=['GET'])
# @auth
# def get_default_addr():
#     user = User.query.filter_by(id=get_userId(request)).first()
#     addr = Address.query.filter_by(is_default=True, user_id=user.id).first()
#     if addr:
#         return jsonify({'success': True, 'data': [dict(addr)]})

#     if user.address:
#         addr = dict(user.address[0])
#     return jsonify({'success': True, 'data': [addr]})
