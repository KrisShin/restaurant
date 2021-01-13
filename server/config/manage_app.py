from flask import Flask
from .db_config import DBConfig
from flask_sqlalchemy import SQLAlchemy
from .global_params import DB


def create_app():
    '''Create an application of flask'''

    app = Flask(__name__)
    app.config.from_object(DBConfig)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='di*nq30($jkfvm.oh0v09ase0',
        ENV='development',
    )
    # register blurprint
    # app.register_blueprint(blueprint=route_teacher, url_prefix='/')
    # app.register_blueprint(blueprint=route_student, url_prefix='/student')
    # app.register_blueprint(blueprint=route_class, url_prefix='/class')
    # app.register_blueprint(blueprint=route_grade, url_prefix='/grade')
    # app.register_blueprint(blueprint=route_dormitory, url_prefix='/dormitory')
    # app.register_blueprint(blueprint=route_admin, url_prefix='/admin')

    app.config['SECRET_KEY'] = 'q7t4gfsg*nj978*n!2%^.uo18sgr'
    DB = SQLAlchemy(app)

    return app
