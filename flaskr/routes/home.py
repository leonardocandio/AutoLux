from flask import Blueprint, render_template
from utils.db import db
from models.car import Car
from models.user import User
from auth import login_required, admin_role_required

menu = Blueprint('menu', __name__)

#Rutas de prueba
@menu.route('/')
@login_required
def home():
    return render_template("index.html")

@menu.route('/add_car')
def add_car():
    car = Car('TOYOTA RAP4')
    db.session.add(car)
    db.session.commit()
    return 'Car added successfully'

@menu.route('/add_user')
def add_user():
    user = User("SomeUser", "password1", "user")
    db.session.add(user)
    db.session.commit()
    return 'User added successfully'

@menu.route('/delete_user/<id>')
@admin_role_required
def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return 'User deleted successfully'

@menu.route('/test')
@admin_role_required
def test():
    return render_template('base.html')