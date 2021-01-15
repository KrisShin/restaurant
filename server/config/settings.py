import os

# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# upload file absolute directory
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

SALT = '0.3qxl9vc_j7kv!ja'

REDIS_USER = ''
REDIS_PWD = ''#'R3D1Sus#r'
REDIS_HOST = 'localhost'
REDIS_PORT = '16379'
REDIS_DB = 0

EMAIL_ACCOUNT = '2855829886@qq.com'
EMAIL_AUTH = 'tdlzctihcooodgbc'