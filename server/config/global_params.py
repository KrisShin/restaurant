from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


# sqlalchemy object
db = SQLAlchemy()

# redis client
redis = FlaskRedis()
