from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(15), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    role = SelectField('Role', choices=[('contestant', 'Contestant'), ('organizer', 'Organizer')], validators=[InputRequired()])
    submit = SubmitField('Register')



@app.route('/')
def home():
    return render_template('base/base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', form=form, error='Invalid credentials')

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        role = form.role.data

        if role == 'contestant':
            return redirect(url_for('contestant_login'))
        elif role == 'organizer':
            return redirect(url_for('organizer_login'))

    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/create_tournament')
def create_tournament():
    if current_user.role != 'organizer':
        return redirect(url_for('login'))

    return render_template('create_tournament.html')

# @app.route('/contestant_page')
# def contestant_page():
#     if current_user.role != 'contestant':
#         return redirect(url_for('login'))

#     return render_template('contestant_page.html')

# @app.route('/organizer_page')
# @login_required
# def organizer_page():
#     if current_user.role != 'organizer':
#         return redirect(url_for('login'))

    return render_template('organizer_page.html')

@app.route('/contestant_login')
def contestant_login():
    return render_template('contestant_login.html')

@app.route('/organizer_login')
def organizer_login():
    return render_template('organizer_login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
