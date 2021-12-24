from datetime import datetime
from config.global_params import db
from config.settings import TAG_COLOR
from apps.models import BaseModel


dishes = db.Table(
    'rs_dish_order',
    db.Column('dish_id', db.Integer, db.ForeignKey('tb_dish.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('tb_order.id'), primary_key=True),
)


class Order(BaseModel):
    '''Order Model.'''

    __tablename__ = 'tb_order'
    money = db.Column(db.Float, default=0.0)
    # 1-待支付/2-已支付/3-已接单/4-已评价/5-已完成/6-申请退款/0-已取消
    status = db.Column(db.Integer, default=1)
    note = db.Column(db.String(256))  # 备注
    dish_amount = db.Column(db.JSON(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('tb_address.id'))
    dishes = db.relationship(
        'Dish',
        secondary=dishes,
        lazy='subquery',
        backref=db.backref('orders', lazy=True),
    )
    comment = db.relationship("Comment", backref="order", lazy=True, uselist=False)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(**kwargs)

    def keys(self):
        return (
            'id',
            'money',
            'status',
            'status_desc',
            'note',
            'create_time',
            'update_time',
            'address',
            'index_img',
            'amount',
            'dishes',
            'status_color',
        )

    def __getitem__(self, item):
        if item == 'status_desc':
            if self.status == 0:
                return '已取消'
            elif self.status == 1:
                return '未支付'
            elif self.status == 2:
                return '已支付'
            elif self.status == 3:
                return '已接单'
            elif self.status == 4:
                return '待评价'
            elif self.status == 5:
                return '已完成'
            elif self.status == 6:
                return '退款中'
        elif item == 'status_color':
            return TAG_COLOR[self.status]
        elif item == 'name':
            return self.address.name
        elif item == 'address':
            return dict(self.address)
        elif item == 'index_img':
            return dict(self.dishes[0])['index_img']
        elif item == 'update_time':
            if not self.update_time:
                return '待商家接单'
            else:
                return datetime.strftime(self.update_time, '%Y-%m-%d %H:%M:%S')
        elif item == 'create_time':
            return datetime.strftime(self.create_time, '%Y-%m-%d %H:%M:%S')

        elif item == 'amount':
            return sum(self.dish_amount.values())
        elif item == 'dishes':
            dish_list = []
            for dish in self.dishes:
                dict_dish = dict(dish)
                dict_dish['count'] = self.dish_amount[str(dish.id)]
                dish_list.append(dict_dish)
            return dish_list

        return getattr(self, item)


class Comment(BaseModel):
    '''Comment Model.'''

    __tablename__ = 'tb_comment'
    content = db.Column(db.String(512))  # 内容
    rate = db.Column(
        db.Enum('good', 'normal', 'bad', name='rate_enum'), default='good'
    )  # 1-好评/2-中评/3-差评

    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("tb_order.id"))

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(**kwargs)
