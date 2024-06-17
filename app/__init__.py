from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Создаём объект Flask
app = Flask(__name__)

# Устанавливаем секретный ключ
app.config['SECRET_KEY'] = 'my_secret_key'

# Настраиваем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # site.db - название нашей БД, с которой будем работать

# Создаём объект SQLAlchemy
db = SQLAlchemy(app)

# Создаём объект Bcrypt
bcrypt = Bcrypt(app)

# Создаём объект LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Модуль будет перенаправлять пользователя на маршрут, который мы указываем (на авторизацию)

from app import routes
