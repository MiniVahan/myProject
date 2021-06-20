# project/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

##################################################################
###DATABASE SETUP ################################################
##################################################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##################################################################
# LOGIN CONFIGS
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

##################################################################
from my_project.requests import Players, Player
api = Api(app)

api.add_resource(Player,'/details/<string:name>/<email>/<password>/<number>')
api.add_resource(Players,'/list')

##################################################################
from my_project.core.views import core
from my_project.users.views import users
from my_project.blog_posts.views import blog_posts
from my_project.error_pages.handlers import error_pages
from my_project.games.views import games
from my_project.games.millioner.views import mill


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
app.register_blueprint(games)
app.register_blueprint(mill)


