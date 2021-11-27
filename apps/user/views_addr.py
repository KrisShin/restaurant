from flask import Blueprint, request, jsonify

from .models import Address
from config import status_code
from utils.wraps import auth, get_current_user

address = Blueprint('Address', __name__, url_prefix='/customer/addr')


@address.route('/<int:addr_id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def oprate_address(addr_id):
    '''All operation of address'''
    if request.method == 'GET':
        '''Get an addres.'''
        addr = Address.query.filter_by(id=addr_id).first()
        if addr:
            return jsonify({'code': status_code.OK, 'data': dict(addr)})
        else:
            return jsonify({'code': status_code.ADDR_NOT_EXISIT, 'msg': '地址不存在'})

    if request.method == 'POST':
        '''Create an address'''
        if addr_id != 0:
            return jsonify({'code': status_code.ADDR_DATA_ERROR, 'msg': '参数错误'})
        data = request.get_json()
        user = get_current_user()
        addr = Address()
        addr = operate_an_addr(addr, user, data)
        if not addr:
            return jsonify({'code': status_code.PARAM_LACK, 'msg': '缺少参数'})
        addr.save()
        return jsonify({'code': status_code.OK})

    if request.method == 'PUT':
        '''Modify infomation of address'''
        if addr_id == 0:
            return jsonify({'code': status_code.ADDR_DATA_ERROR, 'msg': '参数错误'})
        addr = Address.query.filter_by(id=addr_id).first()
        data = request.get_json()
        user = get_current_user()
        addr = operate_an_addr(addr, user, data)
        if not addr:
            return jsonify({'code': status_code.PARAM_LACK, 'msg': '缺少参数'})
        addr.save()
        return jsonify({'code': status_code.OK})

    if request.method == 'DELETE':
        '''Delete the address'''
        addr = Address.query.filter_by(id=addr_id).first()
        addr.delete()
        return jsonify({'code': status_code.OK})


@address.route('/list/', methods=["GET"])
@auth
def get_addr_by_id():
    '''All address list.'''
    user = get_current_user()
    addrs = [dict(addr) for addr in user.address]
    return jsonify({'code': status_code.OK, 'data': {'addresses': addrs}})


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
        'areaCode': data.get('areaCode'),
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
    addr.name = (name,)
    addr.phone = phone
    addr.location = location
    addr.user = user
    addr.is_default = is_default
    return addr


# @address.route('/getDefault', methods=['GET'])
# @auth
# def get_default_addr():
#     user = get_current_user()
#     addr = Address.query.filter_by(is_default=True, user_id=user.id).first()
#     if addr:
#         return jsonify({'code': status_code.OK, 'data': [dict(addr)]})

#     if user.address:
#         addr = dict(user.address[0])
#     return jsonify({'code': status_code.OK, 'data': [addr]})
