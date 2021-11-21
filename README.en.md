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
4.  cd .. , import test data in db_data folder: psql -U restuser -h localhost -p 35432 -d restaurant -f db_data/public.sql
5.  run server: python manage.py
6.  default administrator account: 13355553333/admin123, default user account: 13344443333/user123.

##### front side (developing)
cd front
1.  npm i
2.  npm run serve

##### mobile side (developing)
cd mobile
1.  npm i
2.  npm run serve
