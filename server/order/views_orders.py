from flask import Blueprint, jsonify, request
from config.global_params import db
from config.status_code import *
from utils.wraps import auth, get_userId
from user.models import User, Address
from dish.models import Dish
from .models import Order, Comment

order = Blueprint('Order', __name__, url_prefix='/order')


@order.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth
def operate_order():
    if request.method == 'GET':
        return jsonify({'success': True})
    if request.method == 'PUT':
        return jsonify({'success': True})
    if request.method == 'POST':
        data = request.get_json()
        dish_ids = data.get('dishes')
        if not dish_ids:
            return jsonify({'success': False, 'code': ORDER_NO_DISH})
        order = Order(
            dishes=Dish
        )
        return jsonify({'success': True})
    if request.method == 'DELETE':
        return jsonify({'success': True})


@order.route('/list', methods=['GET'])
@auth
def get_order_list():
    user = User.query.filter_by(id=get_userId(request)).first()
    orders = Order.query.filter_by(user=user).all()
    return jsonify({'success': True, 'data': {'orders': orders}})
