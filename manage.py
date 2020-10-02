from app import create_app, db
from flask_script import Manager, Server, Shell
from app.models import User
# from .models import User
from flask_migrate import Migrate, MigrateCommand

# creating an app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

manager.add_command('server',Server)

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)

if __name__ == '__main__':
    manager.run()