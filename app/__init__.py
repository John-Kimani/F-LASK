from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def createapp(config_class=Config):
    '''
    Factory function
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)


    bootstrap.init_app(app)
    migrate.init_app(app, db)

    
    '''
    Registering blueprints
    '''
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.errors import errors as errors_bp
    app.register_blueprint(errors_bp)

    return app