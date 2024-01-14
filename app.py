from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {
    'organizer@example.com': {'password': 'password', 'role': 'organizer'},
    'contestant@example.com': {'password': 'password', 'role': 'contestant'}
}

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in users and users[email]['password'] == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        if email not in users:
            users[email] = {'password': password, 'role': role}
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('register.html', error='Email already registered')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']
    role = users[user]['role']

    return render_template('dashboard.html', user=user, role=role)

@app.route('/create_tournament')
def create_tournament():
    if 'user' not in session or users[session['user']]['role'] != 'organizer':
        return redirect(url_for('login'))

    return render_template('create_tournament.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
