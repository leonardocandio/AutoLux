from flask import Blueprint

news = Blueprint('news', __name__, template_folder="templates", url_prefix="/news")
