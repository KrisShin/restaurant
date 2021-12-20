from flask import Flask
from flask_cors import CORS

from apps.dish.views_dish import dish as customer_dish
from apps.order.views_order import order as customer_order
from apps.user.views_addr import address as customer_addr
from apps.user.views_user import user as customer_user
from apps.user.views_merchant import merchant as merchant_user
from apps.dish.views_dish_merchant import dish as merchant_dish
from .db_config import DBConfig
from .global_params import db, redis
from .settings import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PWD, REDIS_DB, STATIC_FOLDER, STATIC_PATH


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                static_url_path=STATIC_PATH)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='di*nq30($jkf(msqp>vm.oh5v79ase0',
        ENV='development',
        REDIS_URL=f"redis://{REDIS_USER}:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
    )

    register_blueprint(app)
    db.init_app(app)
    redis.init_app(app)

    CORS(app, supports_credentials=True, resources=r'/*')
    return app


def register_blueprint(app):
    '''Register all the blueprints from apps.'''
    app.register_blueprint(customer_user)
    app.register_blueprint(customer_addr)
    app.register_blueprint(customer_dish)
    app.register_blueprint(customer_order)
    app.register_blueprint(merchant_user)
    app.register_blueprint(merchant_dish)
