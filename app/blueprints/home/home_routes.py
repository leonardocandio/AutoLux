from flask import render_template
from flask_login import login_required, current_user

from app.blueprints.auth.models.role import Permission
from app.blueprints.home.controller import home


# Rutas de prueba
@home.route('/')
@login_required
def home_page():
    return render_template("index.html")


#
# @home.route('/add_car')
# def add_car():
#     car = Car('TOYOTA RAV4')
#     db.session.add(car)
#     db.session.commit()
#     return 'Car added successfully'
#
# @home.route('/add_user')
# def add_user():
#     user = User("SomeUser", "password1", "user")
#     db.session.add(user)
#     db.session.commit()
#     return 'User added successfully'
#
# @home.route('/delete_user/<id>')
# @admin_required
# def delete_user(id):
#     User.query.filter_by(id=id).delete()
#     db.session.commit()
#     return 'User deleted successfully'
#
# @home.route('/test')
# @admin_required
# def test():
#     return render_template('base.html')
@home.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
