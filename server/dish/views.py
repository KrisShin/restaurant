from flask import Blueprint, jsonify, request
from .models import Dish, Tag
from user.models import User
from utils.util import make_password
from utils.wraps import get_userId
from config.global_params import db

dish = Blueprint('Dish', __name__, url_prefix='/dish')


# @dish.route('', methods=['POST', 'GET'])
# def add_tags():
#     tags = ['蛋糕', '奶茶', '碳酸饮料', '偏甜', '咸香', '香辣', '麻辣', '特辣', '微辣',
#             '中辣', '广东辣', '少油', '少盐', '少糖', '甜点', '海鲜', '生鲜', '五香', '糖醋']
#     for t in tags:
#         tag = Tag(name=t)
#         db.session.add(tag)
#         db.session.commit()
#     return jsonify({'msg':'OK'})

@dish.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'GET':
        ex_tags = []
        user_id = get_userId(request)
        ex_ids = []
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            ex_tags = [dict(tag) for tag in user.tags]
            ex_ids = [tag['id'] for tag in ex_tags]
            
        res = [dict(tag) for tag in Tag.query.filter(Tag.id.notin_(ex_ids)).all()]
        return jsonify({'success': True, 'data': {
            'tags': res,
            'exist_tags': ex_tags
        }})
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')

        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()

        return jsonify({'success': True, 'data': dict(tag)})
