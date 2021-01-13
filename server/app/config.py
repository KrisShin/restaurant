import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base config"""
    DEBUG = False
    DB_SERVER = 'localhost'
    ENV = 'development'

    @property
    def DATABASE_URI(self):
        return 'postgresql://flask_server:12345@{}/videocommunity'.format(self.DB_SERVER)