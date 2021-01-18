from flask import Blueprint, jsonify, request
from .models import Dish, Tag
from utils.util import make_password
from config.global_params import db

dish = Blueprint('Dish', __name__, url_prefix='/dish')


@dish.route('', methods=['POST', 'GET'])
def add_tags():
    tags = ['蛋糕', '奶茶', '碳酸饮料', '偏甜', '咸香', '香辣', '麻辣', '特辣', '微辣',
            '中辣', '广东辣', '少油', '少盐', '少糖', '甜点', '海鲜', '生鲜', '五香', '糖醋']
    for t in tags:
        tag = Tag(name=t)
        db.session.add(tag)
        db.session.commit()
    return jsonify({'msg':'OK'})
