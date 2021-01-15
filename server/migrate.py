from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config.manage_app import create_app
from config.global_params import db
import user.models
import dish.models
import order.models


if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
