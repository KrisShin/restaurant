from flask import Flask
from flask_login import LoginManager
from .db_config import DBConfig
from .global_params import db, redis
from .settings import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PWD, REDIS_DB
from user.views import user
from dish.views import dish
from order.views import order


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='di*nq30($jkf(msqp>vm.oh0v09ase0',
        ENV='development',
        REDIS_URL=f"redis://{REDIS_USER}:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    )

    register_blueprint(app)
    db.init_app(app)
    redis.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    return app


def register_blueprint(app):
    '''注册路由蓝图'''
    app.register_blueprint(user)
    app.register_blueprint(dish)
    app.register_blueprint(order)
