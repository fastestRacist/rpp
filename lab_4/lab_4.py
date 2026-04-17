from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'секретно-секретный секрет'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if email == '' or password == '':
            return render_template('login.html', error = 'Заполните все поля')

        user = User.query.filter_by(email=email).first()

        if not user:
            return render_template('login.html', error = 'Пользователь с такой почтой не найден')

        if user.password != password:
            return render_template('login.html', error = 'Неверный пароль')

        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name == '' or email == '' or password == '':
            return render_template('signup.html', error = 'Заполните все поля')

        user = User.query.filter_by(email=email).first()

        if user:
            return render_template('signup.html', error = 'Такой пользователь уже есть')

        new_user = User(name=name, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)