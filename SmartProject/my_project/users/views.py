# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from flask_login import login_user, current_user, logout_user, login_required
from my_project import db
from my_project.models import User
from my_project.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from my_project.users.picture_handler import add_profile_pic
from random import randrange
from my_project import app
from flask_mail import Mail, Message

users = Blueprint('users', __name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'minivahan@gmail.com'
app.config['MAIL_PASSWORD'] = 'passwordforpython'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        value = randrange(100000, 999999, 1)
        session['code'] = value
        email = form.email.data
        subject = 'Verification code number'
        msg = f'Your verification code number is` {value}'

        message = Message(subject, sender="minivahan@gmail.com", recipients=[email])
        message.body = msg

        mail.send(message)
        return render_template('verification.html')
    return render_template("register.html", form=form)


# verification
@users.route('/verification', methods=['GET', 'POST'])
def verif():
    if int(request.form['number']) == int(session['code']):
        user = User(email=session['email'], username=session['username'], password=session['password'])
        db.session.add(user)
        db.session.commit()
        flash("Account registered successfully!")
        return redirect(url_for("users.login"))
    else:
        return redirect(url_for("users.verif"))


# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('mill.millioner')
            return redirect(next)
    return render_template('login.html', form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Updated!")
        return redirect(url_for("users.account"))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


@users.route("/dashboard")
def check_dashboard():
    page = request.args.get("page", 1, type=int)
    users = User.query.all()
    users = sorted(users, key=lambda x: int(x.numbers), reverse=True)
    return render_template('dashboard.html', users=users, page=page)
