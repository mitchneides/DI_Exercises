from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = random._urandom(56)


# Database Connection
db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': 'Hameri16!',
           'user': 'mitch',
           'port': ''}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes

