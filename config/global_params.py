from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy object
db = SQLAlchemy()

# redis client
redis = FlaskRedis()
