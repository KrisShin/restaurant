from datetime import datetime
import json
from flask import Blueprint, jsonify, request

from utils.util import save_img
from .models import Discount, Dish, DishImg, Tag
from config import status_code
from utils.wraps import auth

dish = Blueprint('DishMerchant', __name__, url_prefix='/merchant/dish')


@dish.route('/<string:dish_id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth
def operate_dish(dish_id):
    if request.method == 'GET':
        dish_obj = Dish.query.filter_by(id=dish_id).first()
        if not dish_obj:
            return jsonify({'code': status_code.DISH_NOT_EXISIT, 'msg': '菜品不存在'})
        return jsonify({'code': status_code.OK, 'data': dict(dish_obj)})
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        images = request.files.getlist('images')
        name = data.get('name')
        price = float(data.get('price', 0))
        description = data.get('description')
        discount_type = int(data.get('discountType', 0))
        tag_id_list = data.get('tags')
        if not all((name, price >= 0, images)):
            return jsonify({'code': status_code.PARAM_LACK, 'msg': '菜品名字, 价格, 首图必传'})
        dish_obj = Dish(name=name, price=price, description=description)
        dish_obj.tags = Tag.query.filter(Tag.id.in_(tag_id_list)).all()
        dish_obj.save()

        discount_obj = Discount(
            description='无折扣',
            discount_type=discount_type,
            dish_id=dish_obj.id,
        )
        if discount_type:
            discount_obj.description = data.get('discountDesc')
            discount_obj.start_time = data.get('startTime')
            discount_obj.end_time = data.get('endTime')
            discount_obj.discount = data.get('discount')
        discount_obj.save()
        
        for index, img_base64 in enumerate(images):
            img_uri = save_img('dish', img_base64)
            img = DishImg(
                uri=img_uri, is_index=int(index == 0), dish_id=dish_obj.id
            )
            img.save()
        return jsonify({'code': status_code.OK})
    if request.method == 'PUT':
        data = json.loads(request.form.get('data'))
        dish_id = data.get('id')
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        tag_id_list = data.get('tags')
        dish_obj = Dish.query.filter_by(id=dish_id).first()
        if not dish_obj:
            return jsonify({'code': status_code.DISH_NOT_EXISIT, 'msg': '菜品不存在'})

        if tag_id_list:
            tags = Tag.query.filter(Tag.id.in_(tag_id_list)).all()
            dish_obj.tags = tags
        if name:
            dish_obj.name = name
        if price:
            dish_obj.price = float(price)
        if description:
            dish_obj.description = description
        dish_obj.save()

        return jsonify({'code': status_code.OK})
    data = request.get_json()
    if request.method == 'DELETE':
        dish_id = data.get('dish_id')
        dish_obj = Dish.query.filter_by(id=dish_id).first()
        if not dish_obj:
            return jsonify({'code': status_code.DISH_NOT_EXISIT, 'msg': '菜品不存在'})
        dish_obj.delete()
        return jsonify({'code': status_code.OK})
