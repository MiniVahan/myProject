# models.py
from my_project import db, login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_restful import Resource, Api
from datetime import datetime

api = Api(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    numbers = db.Column(db.String(64), default=0)

    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "Username {}".format(self.username)


class BlogPost(db.Model):
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return "Post ID: {} -- Date: {} --- {}".format(self.id, self.date, self.title)


class Player(Resource):
    def get(self, name, email, password, number):
        user = User.query.filter_by(username=name).first_or_404(description='There is no data with {}'.format(name))
        return {'id': user.id,
                'username': user.username,
                'email': user.email,
                'score': user.numbers}

    def post(self, name, email, password, number):
        user = User(email=email, username=name, password=password)
        user.numbers = number
        db.session.add(user)
        db.session.commit()
        return user.username+' user successfully registered'

    def put(self, name, email, password, number):
        user = User.query.filter_by(username=name).first_or_404(description='There is no data with {}'.format(name))
        user.numbers = number
        user.email = email
        user.password_hash = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        return "User has been updated!"

    def delete(self, name, email, password, number):
        user = User.query.filter_by(username=name).first_or_404(description='There is no data with {}'.format(name))
        db.session.delete(user)
        db.session.commit()
        return 'User has been deleted'


# api.add_resource(Player, '/player/<string:name>')
api.add_resource(Player, '/player/<string:name>/<email>/<password>/<number>')
