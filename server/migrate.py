from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config.manage_app import create_app
from config.global_params import DB as db
import user.models


if __name__ == '__main__':
    app = create_app()
    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
