from config.settings import SALT
from hashlib import md5

def make_password(password):
    pwd = SALT + password
    return md5(pwd.encode()).hexdigest()
    