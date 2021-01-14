from config.settings import SALT
from hashlib import md5

def make_password(password) -> str:
    '''Generate password with salt.'''
    pwd = SALT + password
    return md5(pwd.encode()).hexdigest()
    
def check_password(password, real_password) -> bool:
    '''Check password.'''
    pwd = make_password(password)
    return real_password == pwd
