from datetime import timedelta

from flask import Flask
from .db_config import DBConfig
from .global_params import db, redis
from .settings import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PWD, REDIS_DB, STATIC_FOLDER, STATIC_PATH
from user.views import user
from dish.views import dish
from order.views import order
from flask_cors import CORS


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                static_url_path=STATIC_PATH)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='di*nq30($jkf(msqp>vm.oh0v09ase0',
        ENV='development',
        REDIS_URL=f"redis://{REDIS_USER}:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    )
    app.permanent_session_lifetime = timedelta(minutes=30) # 设置session到期时间

    register_blueprint(app)
    db.init_app(app)
    redis.init_app(app)

    CORS(app, supports_credentials=True)
    return app


def register_blueprint(app):
    '''注册路由蓝图'''
    app.register_blueprint(user)
    app.register_blueprint(dish)
    app.register_blueprint(order)
