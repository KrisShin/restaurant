# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config.manage_app import create_app
from config.global_params import db
from user.models import User, Address
from dish.models import Dish, Tag
from order.models import Order, Comment


if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
