from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)


    bootstrap.init_app(app)

    
    '''
    Registering blueprints
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    return app