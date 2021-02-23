from base64 import b64decode
from hashlib import md5
import random
import smtplib
import string
from uuid import uuid4

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import SALT, TAG_COLOR


def make_password(password) -> str:
    '''Generate password with salt.'''
    pwd = SALT + password
    return md5(pwd.encode()).hexdigest()


def check_password(password, real_password) -> bool:
    '''Check password.'''
    pwd = make_password(password)
    return real_password == pwd


def gen_filename(ext):
    return uuid4().hex + ext


def save_img(path, base64_str):
    undeal_str, img_content = base64_str.split(',')
    ext = r'.' + undeal_str[11:-7]
    filename = gen_filename(ext)
    with open(f'statics/{path}/{filename}', 'wb') as fp:
        img = b64decode(img_content)
        fp.write(img)
    return path.replace('statics', '/static')


def get_captcha():
    return ''.join(random.choices(string.digits+string.ascii_letters, k=8))


def set_tag_color(tags):
    for t in tags:
        t['color'] = TAG_COLOR[t['weight']]
    return tags
