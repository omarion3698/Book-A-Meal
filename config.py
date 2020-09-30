import os

class Config:

    MEAL_API_BASE_URL ='https://api.themealdb.org/3/MEAL/{}?api_key={}'
    MEAL_API_KEY = os.environ.get('MEAL_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
