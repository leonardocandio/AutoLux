from flask import render_template

from app.blueprints.shop.controller import shop
from .models.car import Car
from .models.brand import Brand
from ..auth.models.role import Permission
from .filter import filter


@shop.route('/')
def home():
    cars = Car.query.all()
    return render_template('shop.html', cars=cars)

@shop.route('/<search>', methods=['GET', 'POST'])
def home_search(search = ""):
    cars = Car.query.all()
    cars = filter(cars, search)
    return render_template('shop.html', cars=cars)

@shop.route('/<car_id>')
def product_page(car_id):
    car = Car.query.filter_by(id=car_id).first()
    return render_template('review_car.html', car=car)


@shop.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
