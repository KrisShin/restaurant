from flask import Blueprint, jsonify, request

from utils.util import save_img
from .models import Dish, DishImg, Tag
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
        Dish.query.order_by(Dish.update_time.desc(), Dish.create_time.desc())
        .paginate(page, 5)
        .items
    )

    dishes = [dict(dish) for dish in dishes]
    return jsonify({'code': status_code.OK, 'data': dishes})


@dish.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def operate_dish():
    if request.method == 'GET':
        data = request.args
        dish_id = data.get('id')
        dish_obj = Dish.query.filter_by(id=dish_id).first()
        if not dish_obj:
            return jsonify({'code': status_code.DISH_NOT_EXISIT, 'msg': '菜品不存在'})
        return jsonify({'code': status_code.OK, 'data': dict(dish_obj)})
    data = request.get_json()
    if request.method == 'POST':
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        discount_id = data.get('discount_id')
        tag_id_list = data.get('tag_id_list')
        images = data.get('images')
        if not all((name, price >= 0, images)):
            return jsonify({'code': status_code.PARAM_LACK, 'msg': '菜品名字, 价格, 首图必传'})
        dish_obj = Dish(
            name=name, price=price, description=description, discount_id=discount_id
        )
        tags = Tag.query.filter(Tag.id.in_(tag_id_list)).all()
        dish_obj.tags = tags
        dish_obj.save()
        for index, img_base64 in enumerate(images):
            img_uri = save_img('dish', img_base64)
            img = DishImg.query.create(
                uri=img_uri, is_index=index == 0, dish_id=dish_obj.id
            )
            img.save()
        return jsonify({'code': status_code.OK})
    if request.method == 'PUT':
        return jsonify({'code': status_code.OK})
    if request.method == 'DELETE':
        return jsonify({'code': status_code.OK})
