from flask import render_template
from .models.car import Car
from app.blueprints.shop import shop


@shop.route('/')
def home():
    cars = Car.query.all()
    return render_template('shop.html', cars=cars)


@shop.route('/<car_id>')
def product_page(car_id):
    car = Car.query.filter_by(id=car_id).first()
    return render_template('review_car.html', car=car)
