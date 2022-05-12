from flask import Blueprint

forum = Blueprint('forum',__name__, template_folder='templates',url_prefix="/forum")