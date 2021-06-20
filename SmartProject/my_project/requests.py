from my_project import db
from werkzeug.security import generate_password_hash
from my_project.models import User
from flask_restful import Resource


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


class Players(Resource):
    def get(self):
        users = User.query.all()
        lst= []
        for user in users:
            my_dict = {'user id': user.id,
                       'Username': user.username,
                       'Email': user.email
                        }
            lst.append(my_dict)
        return lst
