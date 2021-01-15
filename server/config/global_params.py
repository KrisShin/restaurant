from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import LoginManager


# sqlalchemy object
db = SQLAlchemy()

# redis client
redis = FlaskRedis()

# flask login manager
login_manager = LoginManager()
