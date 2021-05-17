# restaurant

#### 介绍
一个餐饮管理项目Demo, 后台使用python flask , 前端采用vue2, 数据库使用postgresql11, 缓存使用redis

#### 软件架构
web管理端+移动端使用Vue
后台使用flask

数据库使用postgresql
缓存使用redis

#### 安装教程

##### server端
首先进入server
1.  pip install -r server/requirements
2.  修改config/settings.py redis的主机和端口密码
3.  修改config/db_config.py postgresql的主机和端口用户密码
4.  退出server, 导入db_data文件夹的测试数据恢复数据库 psql -U restuser -h localhost -p 35432 -d restaurant -f db_data/restaurant.psql
5.  python manage.py 运行服务
6.  默认管理员账户13355553333, 密码admin123, 默认用户:13344443333, 密码:user123

##### front端(开发中)
首先进入front
1.  npm i
2.  npm run serve 运行程序

##### mobile端(开发中)
进入mobile
1.  npm i 安装依赖包
2.  npm run serve 运行程序

数据库备份(系统命令)
pg_dump -U restuser -p 35432 -d restaurant -f db_data/restaurant.psql
