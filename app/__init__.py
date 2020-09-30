from flask import Flask 
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




def create_app(mode):
    app = Flask(__name__)

    # create app configurations
    app.config.from_object(config_options[mode])
    
    # Registering the blueprint
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    # Initializing flask extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)
    
    app.config['SECRET_KEY'] = 'any secret string'
    # setting config
    # from .requests import configure_request
    # configure_request(app)

    # configure UploadSet
    configure_uploads(app,photos)

    return app