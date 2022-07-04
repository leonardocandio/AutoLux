from flask import render_template, abort, request, jsonify
from flask_login import current_user, login_required

from server.app.blueprints.shop.controller import shop
from .models.car import Car
from ..auth.models.role import Permission
from .filter import search_by_name, filter_by

# --------------- PAGINATION -----------------#

ITEMS_PER_PAGE = 9
def paginate(model, request, last_page=False):
    query = Car.query.order_by(model.created_at.desc())

    if last_page:
        page = query.count() // ITEMS_PER_PAGE
    else:
        page = request.args.get('page', 1, type=int)

    return query.paginate(
        page=page, per_page=ITEMS_PER_PAGE, error_out=True)

# --------------- CARS GET -----------------#

@shop.route('/', methods=['GET'])
def get_cars():
    cars = paginate(Car, request)
    try:
        return jsonify({
            'code': 200,
            'success': True,
            'cars': [car.format() for car in cars.items],
            'total_cars': cars.total
        })
    except Exception:
        abort(404)


@shop.route('/', methods=['GET'])
def ger_car():
    car_id = request.args.get('id', type=int)
    car = Car.query.filter_by(id=car_id).first()
    if car:
        return jsonify({
            'code': 200,
            'success': True,
            'cars': car.format()
        })
    else:
        abort(404)


# --------------- CARS POST -----------------#

@shop.route('/', methods=['POST'])
def search_car():
    search = request.args.get('search')
    
    if search:
        cars = Car.query.all()
        cars = search_by_name(cars, search)
        return jsonify({
                'code': 200,
                'success': True,
                'cars': [car.format() for car in cars],
                'total_cars': cars.count()
                })
    else:
        abort(404)


@shop.route('/', methods=['POST'])
def filter_cars():
    start_price = request.args.get('start_price_filter')
    end_price = request.args.get('end_price_filter')
    model = request.args.get('model_filter')
    brand = request.args.get('brand_filter')
    year = request.args.get('year_filter')

    cars = Car.query.all()
    if start_price is not None and end_price is not None:
        cars = filter_by(cars, 'price', [int(start_price), int(end_price)])

    if model is not None:
        cars = filter_by(cars, 'model', model)
    
    if brand is not None:
        cars = filter_by(cars, 'brand', brand)

    if year is not None:
        cars = filter_by(cars, 'year', int(year))

    if cars:
        return jsonify({
            'code': 200,
            'success': True,
            'cars': [car.format() for car in cars],
            'total_cars': cars.count()
        })
    else:
        abort(404)


# --------------- CARS DELETE -----------------#



# @shop.app_context_processor
# def inject_permissions():
#     return dict(Permission=Permission)


# @shop.before_request
# @login_required
# def before_request():
#     if not current_user.is_authenticated:
#         abort(401)
