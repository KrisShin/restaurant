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
    1: '#cccccc',
    2: '#808089',
    3: '#aa3030',
    4: '#ff00ff',
    5: '#0000ff',
    6: '#00ffff',
    7: '#00ff00',
    8: '#cccc00',
    9: '#ff5500',
    10: '#ff0000',
}
