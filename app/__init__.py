from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.account.views import account
from app.main.views import main_home

db = SQLAlchemy()
login = LoginManager()
flask_bcrypt = Bcrypt()
admin = Admin()
#admin.add_view(ModelView(Controller,db.session))
#login_manager.login_view = "account.login_page"
#login_manager.login_message_category = 'info'

def register_extensions(app):
    db.init_app(app)
    login.init_app(app)
    flask_bcrypt.init_app(app)
    admin.init_app(app)

def configure_db(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def configure_user_loader(app):
    @app.login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(account)
    app.register_blueprint(main_home)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
    register_extensions(app)
    configure_db(app)
    configure_user_loader(app)

    return app

