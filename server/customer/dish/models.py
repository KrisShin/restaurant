from datetime import datetime
from config.global_params import db
from config.settings import HTTP_HOST, TAG_COLOR


tags = db.Table('rs_dish_tag',
                db.Column('dish_id', db.Integer, db.ForeignKey(
                    'dish.id'), primary_key=True),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Dish(db.Model):
    __tablename__ = "dish"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, default=0.01)
    amount = db.Column(db.Integer, default=0)  # 销量
    description = db.Column(db.String(256))

    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime)

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('dishes', lazy=True))  # 标签(口味偏好) n:n

    images = db.relationship("DishImg", backref="dish", lazy=True)

    def __init__(self, *args, **kwargs):
        super(Dish, self).__init__(**kwargs)

    def keys(self):
        return ('id', 'name', 'price', 'amount', 'description', 'discount', 'discount_desc', 'tags', 'images', 'index_img')

    def __getitem__(self, item):
        if item == 'discount_desc':
            if self.discount.discount_type == 0:
                return None
            return self.discount.description
        elif item == 'discount':
            return self.discount.discount
        elif item == 'tags':
            return [dict(tag) for tag in self.tags]
        elif item == 'images':
            return [dict(img) for img in self.images]
        elif item == 'index_img':
            for img in self.images:
                if img.is_index:
                    return HTTP_HOST + img.uri
        return getattr(self, item)

    def set_update_time(self):
        self.update_time = datetime.now()


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, default=1)  # 权重:选的人越多, 权重越高
    name = db.Column(db.String(32), unique=True)  # 标签字数不能超过8个字
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(**kwargs)

    def keys(self):
        return ('id', 'weight', 'name', 'color')

    @classmethod
    def update_weight(cls):
        for tag in Tag.query.all():
            tag.weight = len(tag.users)+len(tag.dishes)
            db.session.commit()

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        if item == 'color':
            return TAG_COLOR[self.weight % 10]
        return getattr(self, item)


class Discount(db.Model):
    __tablename__ = 'discount'

    id = db.Column(db.Integer, primary_key=True)
    # 0-没有折扣/1-折扣/2-买一送一/3-第二件半价
    discount_type = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime)
    discount = db.Column(db.Float, default=0.01)

    dishes = db.relationship("Dish", backref="discount", lazy=True)

    def __init__(self, *args, **kwargs):
        super(Discount, self).__init__(**kwargs)


class DishImg(db.Model):
    __tablename__ = 'dishimg'
    id = db.Column(db.Integer, primary_key=True)

    is_index = db.Column(db.Boolean, default=0)
    uri = db.Column(db.String(512), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))

    def __init__(self, **kwargs):
        super(Discount, self).__init__(**kwargs)

    def keys(self):
        return ('id', 'is_index', 'uri')

    def __getitem__(self, item):
        if item == 'uri':
            return HTTP_HOST + getattr(self, item)
        return getattr(self, item)