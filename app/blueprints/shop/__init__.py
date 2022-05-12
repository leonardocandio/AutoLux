from flask import Blueprint

shop = Blueprint('shop', __name__,template_folder="templates",url_prefix="/shop",)


