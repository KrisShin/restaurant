import os

# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_FOLDER = os.path.join(BASE_DIR, 'statics')
STATIC_PATH = '/static'

# upload file absolute directory
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

SALT = r'0.3qxl9vc_j7kv!ja'
KEY = r'734&jai<,oqe).ac*'

REDIS_USER = ''
REDIS_PWD = r"R3D1Su@er"
REDIS_HOST = r'localhost'
REDIS_PORT = r'16379'
REDIS_DB = 0

EMAIL_NICKNAME = r'恰了木有APP'
EMAIL_ACCOUNT = r'2855829886@qq.com'
EMAIL_AUTH = r'tdlzctihcooodgbc'

HTTP_HOST = 'http://127.0.0.1:9096'

TAG_COLOR = {
    0: '#cccccc',
    1: '#808089',
    2: '#aa3030',
    3: '#ff00ff',
    4: '#0000ff',
    5: '#00ffff',
    6: '#00ff00',
    7: '#cccc00',
    8: '#ff5500',
    9: '#ff0000',
}

ORDER_STATUS = {
    0: 'cancelOrder',
    1: 'waitPay',
    2: 'paid',
    3: 'gotOrder',
    4: 'waitComment',
    5: 'doneOrder',
}