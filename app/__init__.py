from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase

# SQLAlchemy 2.x DeclarativeBase kullanımı
class Base(DeclarativeBase):
    pass

# Eklentileri initialize et, ancak app'e bağlama işlemini create_app içinde yap (Application Factory)
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Lütfen bu sayfaya erişmek için giriş yapın.'

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class is None:
        from config import Config
        app.config.from_object(Config)
    else:
        app.config.from_object(config_class)

    # Eklentileri app'e bağla
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Blueprint'leri kaydet
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
from app import models