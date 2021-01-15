from datetime import datetime
from config.global_params import db


class Dish(db.Model):
    __tablename__ = "dish"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, default=0.01)
    amount = db.Column(db.Integer, default=0)  # 销量
    description = db.Column(db.String(256))
    discount_type = db.Column(db.Integer)  # 0-没有折扣/1-折扣/2-买一送一/3-第二件半价
    discount = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    tags = db.relationship("Tag", back_populates='dish')

    def __init__(self, *args, **kwargs):
        super(Dish, self).__init__(**kwargs)


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, default=1)  # 权重:选的人越多, 权重越高
    name = db.Column(db.String(32))  # 标签字数不能超过8个字
    create_time = db.Column(db.DateTime, default=datetime.now)

    users = db.relationship("User", back_populates='tag')
    dishes = db.relationship("Dish", back_populates='tag')

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(**kwargs)


dish_tag_table = db.Table('rs_dish_tag', db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True),
                          db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))
