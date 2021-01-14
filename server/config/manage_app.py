from flask import Flask
from .db_config import DBConfig
from .global_params import DB
from user.views import user


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='di*nq30($jkf(msqp>vm.oh0v09ase0',
        ENV='development',
    )

    register_blueprint(app)

    return app


def register_blueprint(app):
    '''注册路由蓝图'''
    app.register_blueprint(user)
