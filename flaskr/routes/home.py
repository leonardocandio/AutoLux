from flask import Blueprint
from utils.db import db
from models.car import Car

menu = Blueprint('menu', __name__)

#Rutas de prueba
@menu.route('/')
def home():
    return 'Hola Mundo!'

    
@menu.route('/add_car')
def add_car():
    car = Car()
    db.session.add(car)
    db.session.commit()
    return 'car added successfully'

