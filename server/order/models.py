from datetime import datetime
from config.global_params import db
from dish.models import Dish


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    money = db.Column(db.Float, default=0.0)
    status = db.Column(db.Integer, default=1)  # 1-待支付/2-已支付/3-已接单/4-已完成/0-已取消
    note = db.Column(db.String(256))  # 备注
    user = db.relationship("User", back_populates="order")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    address = db.relationship("Address", back_populates="order")
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    dishes = db.relationship("Dish", back_populates="order")  # n:n


dish_order_table = db.Table('rs_dish_order', db.Column('dish_id', db.Integer, db.ForeignKey(
    'dish.id'), primary_key=True), db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(512))  # 内容
    rate = db.Column(db.Enum('good', 'ok', 'bad', name='rate_enum'),
                     default='good')  # 1-好评/2-中评/3-差评

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship('User', back_populates='comment')
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    order = db.relationship('Order', back_populates='comment')
