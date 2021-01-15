# restaurant

#### 介绍
一个私人餐饮管理项目

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
4.  使用flask-migrate 运行migrate.py 迁移数据库(具体教程自行百度)
5.  python manage.py 运行服务
6.  退出server, 导入db_data文件夹的测试数据
7.  默认管理员账户admin, 密码admin123, 默认用户:user, 密码:user123

##### front端
首先进入front
1.  npm i
