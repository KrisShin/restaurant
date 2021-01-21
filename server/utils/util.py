from config.settings import SALT, EMAIL_ACCOUNT, EMAIL_AUTH
from hashlib import md5
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random
import string
from uuid import uuid4
from base64 import b64decode


def make_password(password) -> str:
    '''Generate password with salt.'''
    pwd = SALT + password
    return md5(pwd.encode()).hexdigest()


def check_password(password, real_password) -> bool:
    '''Check password.'''
    pwd = make_password(password)
    return real_password == pwd


def gen_filename(ext):
    return uuid4() + ext


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


class SendServer(object):
    '''A server to send email.'''

    def __init__(self,):
        self.email = EMAIL_ACCOUNT
        self.auth = EMAIL_AUTH

    def _authLogin(self):
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        try:
            server.login(self.email, self.auth)
            return server
        except Exception as e:
            print(e)
            return False

    def _compContent(self, receiver, mail):
        message = MIMEMultipart('related')
        message['Subject'] = mail['subject']
        message['From'] = self.email
        message['To'] = receiver
        text = mail['content']
        content = MIMEText(
            f'<html><body>{text}</body></html>', 'html', 'utf-8')
        message.attach(content)

        return message

    def send(self, receiver, mail) -> bool:
        server = self._authLogin()
        if not server:
            return 0

        msg = self._compContent(receiver, mail)

        try:
            server.sendmail(self.email, receiver, msg.as_string())
            server.quit()
            return True
        except smtplib.SMTPException as e:
            print(e)
            return -1


sender = SendServer()
