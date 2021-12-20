from flask import Blueprint, jsonify, request
from .models import Dish
from config import status_code
from utils.wraps import auth

dish = Blueprint('DishMerchant', __name__, url_prefix='/merchant/dish')


@dish.route('/list/', methods=['POST'])
@auth
def post_dish_list():
    '''All dishes list. Order by dish's update time. and return 5 dishes on per refresh.'''
    data = request.get_json()
    page = data.get('page', 1) or 1
    dishes = (
        Dish.query.order_by(Dish.update_time.desc(), Dish.create_time.desc()).paginate(page, 5).items
    )

    dishes = [dict(dish) for dish in dishes]
    return jsonify({'code': status_code.OK, 'data': dishes})
