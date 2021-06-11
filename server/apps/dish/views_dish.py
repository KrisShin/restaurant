from flask import Blueprint, jsonify, request
from .models import Dish, Tag
from apps.user.models import User
from utils.wraps import auth, get_userId
from config.global_params import db
from utils.rest_redis import r

dish = Blueprint('Dish', __name__, url_prefix='/customer/dish')


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

        res = [dict(tag) for tag in Tag.query.filter(
            Tag.id.notin_(ex_ids)).order_by(Tag.weight.desc()).all()]

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


@dish.route('/push', methods=['GET'])
def push_dishes():
    user = User.query.filter_by(id=get_userId(request)).first()
    push_swiper = []
    push = []
    tags_swiper = []
    tags = []
    if user:
        tags += user.tags
        tags_swiper += tags[:4]
        tags = Tag.query.filter(Tag.id.notin_(
            [t.id for t in user.tags])).order_by(Tag.weight.desc()).all()
        tags_swiper += tags[:6]
    else:
        tags += Tag.query.filter(Tag.weight>0).order_by(Tag.weight.desc()).all()
        tags_swiper += tags[:10]

    ex_dish_ids = []
    for tag in tags:
        for dish in tag.dishes[:3]:
            if dish.id in ex_dish_ids:
                continue
            push.append(dict(dish))
            ex_dish_ids.append(dish.id)

    ex_dish_ids = []
    for tag in tags_swiper:
        for dish in tag.dishes[:3]:
            if dish.id in ex_dish_ids:
                continue
            push_swiper.append(dict(dish))
            ex_dish_ids.append(dish.id)
    dish_count = int(r.get_val('dish_count') or 0)
    return jsonify({'success': True, 'data': {'pushSwiper': push_swiper, 'pushDish': push, 'dishCount': dish_count}})


@dish.route('/list', methods=['POST'])
@auth
def post_dish_list():
    data = request.get_json()
    point = data.get('point', 0)
    dishes = Dish.query.order_by(Dish.update_time.desc(), Dish.create_time.desc()).offset(point).limit(5).all()

    dishes = [dict(dish) for dish in dishes]
    return jsonify({'success': True, 'data': dishes})


@dish.route('/cart', methods=['POST'])
@auth
def post_dish_cart():
    data = request.get_json()
    dish_ids = data.get('dishes', [])
    if not dish_ids:
        return jsonify({'success': True, 'data': None})
    dishes = [dict(dish)
              for dish in Dish.query.filter(Dish.id.in_(dish_ids)).all()]
    return jsonify({'success': True, 'data': dishes})
