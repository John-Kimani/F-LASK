from flask import Flask
from config import Config


def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    '''
    Registering blueprints
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    return app