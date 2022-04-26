from flask import Blueprint, render_template
from models.car import Car

shop = Blueprint('shop', __name__)

@shop.route('/shop')
def shop_page():
    cars = Car.query.all()
    return render_template('shop.html', cars=cars)