from flask import Blueprint, render_template, session
from database import db
from app.blueprints.home import home
from app.blueprints.auth.auth_routes import login_required, admin_role_required


#Rutas de prueba
@home.route('/')
@login_required
def home_page():
    user = session.get('user')

    return render_template("index.html", user=user)
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
# @admin_role_required
# def delete_user(id):
#     User.query.filter_by(id=id).delete()
#     db.session.commit()
#     return 'User deleted successfully'
#
# @home.route('/test')
# @admin_role_required
# def test():
#     return render_template('base.html')