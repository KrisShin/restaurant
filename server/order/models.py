from datetime import datetime
from config.global_params import DB as db
from dish.models import Dish


class Order(db.Model):
    __tablename__ = 'tb_order'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    money = db.Column(db.Float, default=0.0)
    status = db.Column(db.Integer, default=1)  # 1-待支付/2-已支付/3-已接单/4-已完成/0-已取消
    note = db.Column(db.String(256))  # 备注
    user = db.relationship("User", backref="user")
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    address = db.relationship("Address", backref="address")
    address_id = db.Column(db.Integer, db.ForeignKey('tb_address.id'))

    dishes = db.relationship("Dish", backref="dish")  # n:n


dish_order_table = db.Table('rs_dish_order',
                            db.Column('dish_id', db.Integer, db.ForeignKey(
                                'tb_dish.id'), primary_key=True),
                            db.Column('order_id', db.Integer, db.ForeignKey('tb_order.id'), primary_key=True))


class Comment(db.Model):
    __tablename__ = 'tb_comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(512))  # 内容
    rate = db.Column(db.Enum('good', 'ok', 'bad', name='rate_enum'), default='good')  # 1-好评/2-中评/3-差评

    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    user = db.relationship('User', backref='user')
    order_id = db.Column(db.Integer, db.ForeignKey("tb_order.id"))
    order = db.relationship('Order', backref='order')
