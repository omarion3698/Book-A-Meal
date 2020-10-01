from flask import Flask
# from instance.config import app_config
from user_profile.models import User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstap = Bootstrap()

photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])  # Configure app according to the environment
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)
    Migrate(app, db)
    from .auth import auth_blueprint  # include the views, in form of blueprints
    from .meals import meals_blueprint
    from .main import main as main_blueprint
    from .orders import orders_blueprint
    from .menu import menu_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(meals_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(menu_blueprint)
    return app