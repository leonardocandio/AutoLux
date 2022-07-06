from math import ceil
from flask import render_template, abort, request, jsonify
from flask_login import current_user, login_required
from math import ceil

from server.app.blueprints.shop.controller import shop
from .models.car import Car
from ..auth.models.role import Permission
from .filter import search_by_name, filter_by

# --------------- PAGINATION -----------------#

def paginate(query, request, items_per_page=9, last_page=False):
    if last_page:
        page = query.count() // items_per_page
    else:
        page = request.args.get('page', 1, type=int)

    return query.paginate(
        page=page, per_page=items_per_page, error_out=True)

def paginate_array(array, request, items_per_page=9, last_page=False):
    n_pages = (len(array) // items_per_page)+1

    if last_page:
        page = len(array) // items_per_page
    else:
        page = request.args.get('page', 1, type=int)

    num_of_pages = (len(array) // items_per_page) + 1

    if page == num_of_pages:
        _initial_page = (page-1)*items_per_page
        _last_page = len(array)
        return [array[_initial_page:_last_page], n_pages]
    else:
        _initial_page = (page-1)*items_per_page
        _last_page = _initial_page + items_per_page
        return [array[_initial_page:_last_page], n_pages ]
    

# --------------- CARS GET -----------------#

@shop.route('/', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    cars = [car.format() for car in cars]
    [cars, n_pages] = paginate_array(cars, request)
    try:
        return jsonify({
            'code': 200,
            'success': True,
            'cars': cars,
            'total_cars': len(cars),
            'n_pages': n_pages
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
    search = request.args.get('search', None)
    nitems = request.args.get('nitems', None, int)
    
    if search:
        query = Car.query.all()
        cars_searched = search_by_name(query, search, nitems)
        return jsonify({
                'code': 200,
                'success': True,
                'cars': [car.format() for car in cars_searched],
                'total_cars': len(cars_searched)
                })
    
    body = request.get_json()
    if(body):
        start_price = body.get('start_price')
        end_price = body.get('end_price')
        model = body.get('model')
        brand = body.get('brand')
        year = body.get('year')

        cars = Car.query.all()
        n_cars = len(cars)
        if (start_price != '' and end_price != '') and (start_price is not None and end_price is not None):
            cars = filter_by(cars, 'price', [int(start_price), int(end_price)])

        if (model != '') and (model is not None):
            cars = filter_by(cars, 'model', model)
        
        if (brand != '') and (brand is not None):
            cars = filter_by(cars, 'brand', brand)

        if (year != '') and (year is not None):
            cars = filter_by(cars, 'year', int(year))

        if len(cars) == 0:
            abort(404)
        else:
            [cars, n_pages] = paginate_array(cars, request)
            return jsonify({
                'code': 200,
                'success': True,
                'cars': [car.format() for car in cars],
                'total_cars': n_cars,
                'n_pages': n_pages
            })


# --------------- CARS DELETE -----------------#



# @shop.app_context_processor
# def inject_permissions():
#     return dict(Permission=Permission)


# @shop.before_request
# @login_required
# def before_request():
#     if not current_user.is_authenticated:
#         abort(401)
