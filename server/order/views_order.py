from flask import Blueprint, json, jsonify, request
from config.global_params import db
from config.status_code import *
from utils.wraps import auth, get_userId
from user.models import User, Address
from dish.models import Dish
from .models import Order, Comment

order = Blueprint('Order', __name__, url_prefix='/order')


@order.route('/<string:order_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth
def operate_order(order_id):
    if request.method == 'GET':
        return jsonify({'success': True})
    if request.method == 'PUT':
        return jsonify({'success': True})
    if request.method == 'POST':
        data = request.get_json()
        cart = data.get('cart')
        note = data.get('note')
        addr_id = data.get('addrId')
        if not cart:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        cart = json.loads(cart)

        dish_amount = {k: v for k, v in cart.items() if v}
        if not dish_amount:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        user = User.query.filter_by(id=get_userId(request)).first()
        addr = Address.query.filter_by(id=addr_id).first()
        if not addr:
            addr = Address.query.filter(
                Address.user == user, Address.is_default == True).first()
        dishes = Dish.query.filter(Dish.id.in_(dish_amount.keys())).all()
        money = 0
        for dish in dishes:
            money += dish_amount[str(dish.id)] * \
                dish.price*dish.discount.discount
        money = round(money, 2)
        print(dish_amount)

        order = Order(
            note=note,
            money=money,
            dish_amount=dish_amount,
            address=addr,
            user=user,
            dishes=dishes,
        )
        db.session.add(order)
        db.session.commit()
        return jsonify({'success': True})
    if request.method == 'DELETE':
        order = Order.query.filter_by(id=order_id).first()
        order.delete()
        db.session.commit()
        return jsonify({'success': True})


@order.route('/list', methods=['GET'])
@auth
def get_order_list():
    user = User.query.filter_by(id=get_userId(request)).first()
    orders = user.orders
    return jsonify({'success': True, 'data': {'orders': orders}})


@order.route('/status', methods=['GET'])
@auth
def get_order_status():
    user = User.query.filter_by(id=get_userId(request)).first()
    order_status = {
        'waitPay': 0,
        'paid': 0,
        'gotOrder': 0,
        'waitComment': 0,
        'doneOrder': 0,
        'cancelOrder': 0
    }
    for order in user.orders:
        if order.status == 0:
            order_status["cancelOrder"] += 1
        elif order.status == 1:
            order_status["waitPay"] += 1
        elif order.status == 2:
            order_status["paid"] += 1
        elif order.status == 3:
            order_status["gotOrder"] += 1
        elif order.status == 4:
            order_status["waitComment"] += 1
        elif order.status == 5:
            order_status["doneOrder"] += 1
    return jsonify({'success': True, 'data': {'orderStatus': order_status}})
