import os

class Config:
    MEAL_API_BASE_URL ='https://api.themealdb.org/3/MEAL/{}?api_key={}'
    MEAL_API_KEY = os.environ.get('MEAL_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
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
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://omarion:29903299@localhost/DB'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}