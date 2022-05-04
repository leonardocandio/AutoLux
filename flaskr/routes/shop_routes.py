from flask import Blueprint, render_template
from models.car import Car

shop = Blueprint('shop', __name__)

@shop.route('/shop')
def shop_page():
    cars = Car.query.all()
    return render_template('shop.html', cars=cars)

@shop.route('/shop/<car_id>')
def product_page(car_id):
    car = Car.query.filter_by(id=car_id).first()
    return render_template('review_car.html', car=car)