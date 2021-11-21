from flask import Blueprint, json, jsonify, request
from config.global_params import db
from config.status_code import *
from config.settings import (
    ORDER_ACCEPTED,
    ORDER_CANCELED,
    ORDER_COMMNETED,
    ORDER_COMPLETE,
    ORDER_PAID,
    ORDER_REFUNDING,
    ORDER_UNPAY,
    ORDER_STATUS,
    ORDER_STATUS_REVERSE,
)
from utils.wraps import auth, get_userId
from apps.user.models import User, Address
from apps.dish.models import Dish
from .models import Order, Comment

order = Blueprint('Order', __name__, url_prefix='/customer/order')


@order.route('/<string:order_id>/', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth
def operate_order(order_id):
    '''All operations of order.'''
    if request.method == 'GET':
        '''Get an order by ID.'''
        order = Order.query.filter_by(id=order_id).first()
        return jsonify({'success': True, 'data': {'order': dict(order)}})
    if request.method == 'PUT':
        '''Update an Order'''
        # Todo: Is this a function of customer or merchant?
        return jsonify({'success': True})
    if request.method == 'POST':
        '''Create an order, order ID is unnecessary.'''
        data = request.get_json()
        cart = data.get('cart')
        note = data.get('note')
        addr_id = data.get('addrId')
        if not cart:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        cart = json.loads(cart)

        # Get all dish's ID and amount.
        dish_amount = {k: v for k, v in cart.items() if v}
        if not dish_amount:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        user = User.query.filter_by(id=get_userId(request)).first()
        addr = Address.query.filter_by(id=addr_id).first()
        if not addr:
            # if not choose an address, use the default address of the user.
            addr = Address.query.filter(
                Address.user == user, Address.is_default == True
            ).first()
        dishes = Dish.query.filter(Dish.id.in_(dish_amount.keys())).all()
        money = 0
        # Calculate the money.
        # TODO: Support other type of discount, not just discount by percentage.
        for dish in dishes:
            money += dish_amount[str(dish.id)] * dish.price * dish.discount.discount
        money = round(money, 2)

        order = Order(
            note=note,
            money=money,
            dish_amount=dish_amount,
            address=addr,
            user=user,
            dishes=dishes,
        )
        order.save()
        return jsonify({'success': True, 'data': {'id': order.id}})
    if request.method == 'DELETE':
        # Delete the order.
        order = Order.query.filter_by(id=order_id).first()
        order.delete()
        return jsonify({'success': True})


@order.route('/list/', methods=['POST'])
@auth
def post_order_list():
    '''Get many types of orders list.'''
    user = User.query.filter_by(id=get_userId(request)).first()
    point = request.get_json().get('point', 0)
    status = request.get_json().get('status')
    if status == 'all' or not status:
        orders = [dict(order) for order in user.orders[point : point + 5]]
    else:
        orders = [
            dict(order)
            for order in user.orders
            if order.status == ORDER_STATUS_REVERSE[status]
        ]
    return jsonify({'success': True, 'data': {'orders': orders}})


@order.route('/status/', methods=['GET'])
@auth
def get_order_status():
    '''Calculate the orders in each status'''
    user = User.query.filter_by(id=get_userId(request)).first()
    order_status_count = {
        'orderUnpay': 0,
        'orderPaid': 0,
        'orderAccept': 0,
        'orderCommented': 0,
        'orderComplete': 0,
        'orderCanceled': 0,
        'orderRefunding': 0,
    }
    for order in user.orders:
        order_status_count[ORDER_STATUS[order.status]] += 1
    return jsonify(
        {
            'success': True,
            'data': {'orderStatus': order_status_count, 'orderCount': len(user.orders)},
        }
    )


@order.route('/pay/', methods=['POST'])
@auth
def post_order_pay():
    '''Pay the order.'''
    id = request.get_json().get('id')
    user = User.query.filter_by(id=get_userId(request)).first()
    order = Order.query.filter_by(id=id).first()
    if user.account.balance < order.money:
        return jsonify({'success': False, 'data': {'message': '余额不足, 请先充值'}})
    user.account.balance -= order.money
    order.status = ORDER_PAID
    order.save()
    user.save()
    return jsonify({'success': True, 'data': {'balance': user.account.balance}})


@order.route('/complete/', methods=['POST'])
@auth
def post_order_complete():
    '''Sign the order is completed.'''
    id = request.get_json().get('id')
    order = Order.query.filter_by(id=id).first()
    if order.status in (ORDER_ACCEPTED, ORDER_COMMNETED):
        order.status = ORDER_COMPLETE
    order.save()
    return jsonify({'success': True})


@order.route('/cancel/', methods=['POST'])
@auth
def post_order_cancel():
    '''Cancel the order'''
    id = request.get_json().get('id')
    user = User.query.filter_by(id=get_userId(request)).first()
    order = Order.query.filter_by(id=id).first()
    msg = ''
    if order.status == ORDER_UNPAY:
        # if order is unpaid, directly set order canceled.
        order.status = ORDER_CANCELED
    elif order.status == ORDER_PAID:
        # if order paid and merchant not accept the order, sign order canceled and refund.
        user.account.balance += order.money
        order.status = ORDER_CANCELED
        user.save()
    elif order.status in (ORDER_ACCEPTED, ORDER_COMMNETED, ORDER_COMPLETE):
        # if order is paid, need merchant confirm then refund to user.
        msg = '等待商家审批退款'
        order.status = ORDER_REFUNDING
    elif order.status in [ORDER_UNPAY, ORDER_REFUNDING]:
        # if order is waiting for merchant confirm.
        msg = '该状态下无法退款, 如有疑问请前往申诉'
    order.save()
    return jsonify({'success': True, 'data': {'message': msg}})
