from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_socketio import SocketIO


db                          = SQLAlchemy()
migrate                     = Migrate()
bootstrap                   = Bootstrap()
# socketio                    = SocketIO()
login_manager               = LoginManager()
login_manager.login_view    = 'auth.login'
login_manager.login_message = 'Please sign in'
login_manager.login_message_category = 'alert-info'
login_manager.refresh_view  = 'auth.refresh'
login_manager.needs_refresh_message = 'Session is closed, please reauthenticate to access this page'
login_manager.needs_refresh_message_category = 'alert-info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)    
    

    # initialization
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)    
    # socketio.init_app(app)
    login_manager.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
        
    return app
    # return socketio.init_app(app)
    

from app import models