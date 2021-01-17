from datetime import datetime
from config.global_params import db
from dish.models import Tag
from order.models import Order, Comment
from flask_login import UserMixin

tags = db.Table('rs_user_tag', db.Column('user_id', db.Integer, db.ForeignKey(
    'user.id'), primary_key=True), db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(128))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    avatar = db.Column(db.String(512))
    email = db.Column(db.String(128), unique=True)  # 邮箱号(辅助找回密码)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Boolean, default=0)  # 性别 0-女/ 1-男
    role = db.Column(db.Enum('user', 'admin', name='role_enum'), default='user') # 权限user(用户)/admin(管理员)
    is_new = db.Column(db.Boolean, default=1)  # 0-否/ 1-是
    is_vip = db.Column(db.Boolean, default=0)
    is_email_active = db.Column(db.Boolean, default=0)  # 是否已激活
    balance = db.Column(db.Float, default=0.0)  # 余额
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    address = db.relationship("Address", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)
    orders = db.relationship("Order", backref="user", lazy=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('users', lazy=True))  # 标签(口味偏好) n:n

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(**kwargs)

    def keys(self):
        '''serilize object keys'''
        return ('id', 'nickname', 'gender', 'is_vip', 'is_email_active', 'is_new', 'balance', 'phone', 'age')

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    location = db.Column(db.String(512), nullable=False)  # 昵称
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    is_delete = db.Column(db.Boolean, default=0)  # 是否已删除

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order = db.relationship("Order", backref="address", lazy=True, uselist=False)


    def __init__(self, *args, **kwargs):
        super(Address, self).__init__(**kwargs)
