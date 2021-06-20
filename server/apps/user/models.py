from datetime import datetime

from config.global_params import db
from config.settings import HTTP_HOST

tags = db.Table('rs_user_tag',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class User(db.Model):
    '''User model'''
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(128))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    avatar = db.Column(db.String(512))
    email = db.Column(db.String(128), unique=True)  # 邮箱号(辅助找回密码)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Boolean, default=0)  # 性别 0-女/ 1-男
    role = db.Column(db.Enum('user', 'admin', name='role_enum'), default='user')  # 权限user(用户)/admin(管理员)
    is_new = db.Column(db.Boolean, default=1)  # 0-否/ 1-是
    account = db.relationship(
        "Account", backref="user", lazy=True, uselist=False)
    is_email_active = db.Column(db.Boolean, default=0)  # 是否已激活
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime)

    address = db.relationship("Address", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)
    orders = db.relationship("Order", backref="user", lazy=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('users', lazy=True))  # 标签(口味偏好) n:n

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(**kwargs)

    def keys(self):
        '''serilize object keys'''
        return (
            'user_id', 'avatar', 'email', 'balance', 'nickname', 'gender', 'is_email_active', 'is_new', 'phone', 'age',
            'tags', 'default_addr')

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        if item == 'user_id':
            return getattr(self, 'id')
        elif item == 'avatar':
            return HTTP_HOST + getattr(self, item)
        elif item == 'balance':
            return self.account.balance
        elif item == 'tags':
            return [dict(tag) for tag in self.tags]
        elif item == 'default_addr':
            for addr in self.address:
                if addr.is_default:
                    return addr.id
            else:
                if self.address:
                    return self.address[0].id
                else:
                    return 0
        return getattr(self, item)

    def set_update_time(self):
        self.update_time = datetime.now()


class Address(db.Model):
    '''Address model'''
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    location = db.Column(db.JSON(), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime)
    is_default = db.Column(db.Boolean, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orders = db.relationship("Order", backref="address", lazy=True)

    def __init__(self, *args, **kwargs):
        super(Address, self).__init__(**kwargs)

    def keys(self):
        return ('id', 'name', 'tel', 'address', 'addressDetail', 'areaCode', 'isDefault')

    def __getitem__(self, item):
        if item == 'tel':
            return self.phone
        elif item == 'isDefault':
            return self.is_default
        elif item == 'addressDetail':
            return self.location.get('addressDetail')
        elif item == 'areaCode':
            return self.location.get('areaCode')
        elif item == 'address':
            return ' '.join(self.location.values())[:-7]

        return getattr(self, item)

    def set_update_time(self):
        self.update_time = datetime.now()

    def delete(self):
        db.session.delete(self)


class Account(db.Model):
    '''User's account'''
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    is_vip = db.Column(db.Boolean, default=0)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    balance = db.Column(db.Float, default=0.0)  # 余额

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(**kwargs)
