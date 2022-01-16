from flask import Blueprint, jsonify, request
from .models import Dish, Tag
from utils.wraps import auth, get_current_user
from utils.rest_redis import r
from config import status_code

dish = Blueprint('Dish', __name__, url_prefix='/customer/dish')


@dish.route('', methods=['POST', 'GET'])
def add_tags():
    '''Add some tags in database.'''
    tags = [
        '蛋糕',
        '奶茶',
        '碳酸饮料',
        '偏甜',
        '咸香',
        '香辣',
        '麻辣',
        '特辣',
        '微辣',
        '中辣',
        '广东辣',
        '少油',
        '少盐',
        '少糖',
        '甜点',
        '海鲜',
        '生鲜',
        '五香',
        '糖醋',
    ]
    for t in tags:
        tag = Tag(name=t)
        tag.save()
    return jsonify({'msg': 'OK'})


@dish.route('/tags/', methods=['GET', 'POST'])
def tags():
    '''All Operations of tag.'''
    if request.method == 'GET':
        '''Get all tags infomation'''
        ex_tags = []
        user = get_current_user(request)
        ex_ids = []
        if user:
            '''If user logined, add user's tags at head of the list'''
            ex_tags = [dict(tag) for tag in user.tags]
            ex_ids = [tag['id'] for tag in ex_tags]

        # Parse all Tags object to dict. And remind tags order by weight.
        res = [
            dict(tag)
            for tag in Tag.query.filter(Tag.id.notin_(ex_ids))
            .order_by(Tag.weight.desc())
            .all()
        ]

        return jsonify(
            {'code': status_code.OK, 'data': {'tags': res, 'exist_tags': ex_tags}}
        )
    if request.method == 'POST':
        '''Create a tag.'''
        data = request.get_json()
        name = data.get('name')

        tag = Tag(name=name)
        tag.save()

        return jsonify({'code': status_code.OK, 'data': dict(tag)})


@dish.route('/push/', methods=['GET'])
def push_dishes():
    '''Get the popular dishes.'''
    user = get_current_user(request)
    push_swiper = []
    push = []
    tags_swiper = []
    tags = []
    if user:
        '''If user logined, add user's first four tag at head of the list'''
        tags += user.tags
        tags_swiper += tags[:4]
        tags = (
            Tag.query.filter(Tag.id.notin_([t.id for t in user.tags]))
            .order_by(Tag.weight.desc())
            .all()
        )
        tags_swiper += tags[:6]
    else:
        tags += Tag.query.filter(Tag.weight > 0).order_by(Tag.weight.desc()).all()
        tags_swiper += tags[:10]

    ex_dish_ids = []
    # Traverse all dishes of the tags.
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
    return jsonify(
        {
            'code': status_code.OK,
            'data': {
                'pushSwiper': push_swiper,
                'pushDish': push,
                'dishCount': dish_count,
            },
        }
    )


@dish.route('/list/', methods=['POST'])
@auth
def post_dish_list():
    '''All dishes list. Order by dish's update time. and return 5 dishes on per refresh.'''
    data = request.get_json()
    page = data.get('page', 1) or 1
    page_size = data.get('pageSize', 5) or 5
    dishes = Dish.query.order_by(Dish.update_time.desc(), Dish.create_time.desc())
    total = dishes.count()

    dishes = [dict(dish) for dish in dishes.paginate(page, page_size).items]
    return jsonify(
        {'code': status_code.OK, 'data': dishes, 'page': page, 'total': total}
    )


@dish.route('/cart/', methods=['POST'])
@auth
def post_dish_cart():
    '''Return dishes which user add in cart.'''
    data = request.get_json()
    dish_ids = data.get('dishes', [])
    if not dish_ids:
        return jsonify({'code': status_code.OK, 'data': None})
    dishes = [dict(dish) for dish in Dish.query.filter(Dish.id.in_(dish_ids)).all()]
    return jsonify({'code': status_code.OK, 'data': dishes})
