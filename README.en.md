# restaurant

#### Description
A restaurant program, backend user Flask framework with python, front use VueJS2, Database is PostgreSQL11, and cache with Redis

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
4.  restore data: psql -U restuser -h localhost -p 35432 -d restaurant -f db_data/restaurant.psql
5.  run server: python manage.py
6.  cd .. , import test data in db_data folder.
7.  default administrator account: admin/admin123, default user account: user/user123.

##### front端
cd front
1.  npm i
