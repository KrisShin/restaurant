# restaurant

#### Description
A personal restaurant program

#### Software Architecture
web and h5: Vue
server: flask
database: postgresql
cache: redis

#### Installation

##### server
cd server
1.  pip install -r server/requirements
2.  modify config/settings.py host,username and password and port of redis.
3.  modify config/db_config.py host,username and password and port of postgresql.
4.  use flask-migrate run migrate.py to migrate database
5.  run server: python manage.py
6.  cd .. , import test data in db_data folder.
7.  default administrator account: admin/admin123, default user account: user/user123.

##### front端
cd front
1.  npm i
