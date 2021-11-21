import os
import random
import string
from base64 import b64decode, decodebytes, encodebytes
from uuid import uuid4

from config.settings import KEY
from Crypto.Cipher import AES

aes = AES.new(str.encode(KEY), AES.MODE_ECB)


def make_password(pwd):
    encode_pwd = str.encode(pwd.rjust(32, '@'))
    encrypt_str = str(encodebytes(aes.encrypt(encode_pwd)), encoding='utf-8')
    return encrypt_str


def check_password(encrypt_str, input_password):
    decrypt_str = (
        aes.decrypt(decodebytes(encrypt_str.encode(encoding='utf-8')))
        .decode()
        .replace('@', '')
    )
    return decrypt_str == input_password


def gen_uuid_name(ext=''):
    return uuid4().hex + ext


def save_img(path, base64_str):
    undeal_str, img_content = base64_str.split(',')
    ext = r'.' + undeal_str[11:-7]
    filename = gen_uuid_name(ext)
    path = f'statics/{path}/{filename}'
    with open(path, 'wb') as fp:
        img = b64decode(img_content)
        fp.write(img)
    return path.replace('statics', '/static')


def del_invalify_image(path):
    if path.lower().endswith('default.jpg'):
        return
    try:
        os.remove(path.replace('/static', 'statics'))
    except Exception as e:
        print(e)


def get_captcha(length=8):
    return ''.join(random.choices(string.digits + string.ascii_letters, k=length))


def get_parse_response(items):
    return [dict(i) for i in items]
