import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://omarion:29903299@localhost/psblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}





















# """This a file to specify the correct app configuration depending on the environment"""
# import os

# class Config(object):
#     """This is the main configuration class"""
#     DEBUG = False
#     SECRET = os.environ.get('SECRET')
#     CSRF_ENABLED = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


# class DevelopmentConfig(Config):
#     """This is the development configuration class"""
#     DEBUG = True


# class TestingConfig(Config):
#     """This is the testing configuration class"""
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'



# class ProductionConfig(Config):
#     """This is the production configuration class"""
#     DEBUG = False
#     TESTING = False


# app_config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
# }