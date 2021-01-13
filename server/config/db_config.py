from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class DBConfig(object):
    """配置参数"""
    # 设置连接数据库的URL
    db_type = 'postgresql'
    user = 'restuser'
    password = 'R35Tus#r'
    database = 'restaurant'
    host = 'localhost'
    port = '35432'

    # 数据库url
    SQLALCHEMY_DATABASE_URI = f'{db_type}://{user}:{password}@{host}:{port}/{database}'

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    # app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    # 设置密钥，用于csrf_token的加解密
    # app.config["SECRET_KEY"] = "xhosd6f982yfhowefy29f"
