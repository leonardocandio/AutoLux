from flask import render_template, abort, request
from flask_login import current_user, login_required

from server.app.blueprints.shop.controller import shop
from .models.car import Car
from ..auth.models.role import Permission
from .filter import filter, filter_by


@shop.route('/')
def home():
    cars = Car.query.all()
    return render_template('shop.html', cars=cars)

@shop.route('/search/<search>', methods=['GET', 'POST'])
def home_search(search = ""):
    cars = Car.query.all()
    cars = filter(cars, search)
    return render_template('shop.html', cars=cars)


@shop.route('/<car_id>')
def product_page(car_id):
    car = Car.query.filter_by(id=car_id).first()
    return render_template('review_car.html', car=car)

@shop.route('/filter', methods=['GET'])
def filter_by_params():
    start_price = request.args.get('start_price_filter')
    end_price = request.args.get('end_price_filter')
    model = request.args.get('model_filter')
    brand = request.args.get('brand_filter')
    year = request.args.get('year_filter')

    cars = Car.query.all()
    if(start_price != "" and end_price  != ""):
        cars = filter_by(cars, 'price', [int(start_price), int(end_price)])

    if(model != ""):
        cars = filter_by(cars, 'model', model)
    
    if(brand != ""):
        cars = filter_by(cars, 'brand', brand)

    if(year != ""):
        cars = filter_by(cars, 'year', int(year))

    return render_template('shop.html', cars=cars)


@shop.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@shop.before_request
@login_required
def before_request():
    if not current_user.is_authenticated:
        abort(401)
