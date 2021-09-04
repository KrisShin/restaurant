from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config.global_params import db
from config.manage_app import create_app

if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
