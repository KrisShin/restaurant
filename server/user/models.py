from datetime import datetime
from config.global_params import DB as db

class User(db.Model):
    __tablename__ = 'tb_user'
 
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(128))
    age = db.Column(db.Integer(3))
    phone = db.Column(db.String(11), unique=True, nullable=False)
    avatar = db.Column(db.String(512))
    email = db.Column(db.String(128), unique=True) # 邮箱号(辅助找回密码)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Enum(0,1))  # 性别 0-女/ 1-男
    role  = db.Column(db.Enum('user','admin'), default='user')  # 权限user(用户)/admin(管理员)
    is_new= db.Column(db.Enum(0,1), defalut=1)  # 0-否/ 1-是
    is_vip = db.Column(db.Enum(0, 1), defalut=0)
    is_actice = db.Column(db.Enum(0, 1), defalut=0)  # 是否已激活
    balance = db.Column(db.Float, default=0.0)  # 余额
    create_time  = db.Column(db.DateTime,default=datetime.now)
    # tags        [Tag]                                   # 标签(口味偏好) n:n
    # address
 
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(**kwargs)
 
    def __repr__(self):
        return f"{self.name}:{self.age}"