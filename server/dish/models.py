from datetime import datetime
from config.global_params import db


tags = db.Table('rs_dish_tag',
                db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True),
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

    def __init__(self, *args, **kwargs):
        super(Dish, self).__init__(**kwargs)


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, default=1)  # 权重:选的人越多, 权重越高
    name = db.Column(db.String(32), unique=True)  # 标签字数不能超过8个字
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(**kwargs)
    
    def keys(self):
        return ('id', 'weight', 'name')
    
    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)


class Discount(db.Model):
    __tablename__ = 'discount'

    id = db.Column(db.Integer, primary_key=True)
    discount_type = db.Column(db.Integer)  # 0-没有折扣/1-折扣/2-买一送一/3-第二件半价
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime)
    discount = db.Column(db.Integer)

    dishes = db.relationship("Dish", backref="discount", lazy=True)
    
    def __init__(self, *args, **kwargs):
        super(Discount, self).__init__(**kwargs)