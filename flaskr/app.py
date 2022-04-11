import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.home import menu
from auth import bp

# recogemos la contraseña
password = f'{sys.argv[1]}'

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost:5432/carsapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping({
    'ENV': 'development',
    'DEBUG': True,
    'TESTING': False,
    'SECRET_KEY': 'secretkey',
})

SQLAlchemy(app)

app.register_blueprint(bp)
app.register_blueprint(menu)




