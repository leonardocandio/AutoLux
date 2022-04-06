from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.home import menu
from utils.db import db

app = Flask(__name__)

#ver que llaves tiene app.config 
print(app.config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost:5432/carsapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping({
    'ENV': 'development',
    'DEBUG': True,
    'TESTING': False,
    'SECRET_KEY': None,
})

SQLAlchemy(app)

app.register_blueprint(menu)


