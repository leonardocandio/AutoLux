from flask import render_template
from werkzeug.exceptions import HTTPException


def error_handlers(app):

    IMAGE_URL = "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png"
    GENERIC_DESCRIPTION = "Parece que la página que estás buscando no existe. No te preocupes, todavía puedes " \
                          "encontrar tu carro de ensueño! "
    PAGE_NOT_FOUND_TITLE = "Página no encontrada"

    @app.errorhandler(400)
    def bad_request(e):
        e = {
            "title": "Solicitud incorrecta",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Algo salio mal, falta algún parámetro o alguno no existe, intente nuevamente.",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(401)
    def auth_required(e):
        e = {
            "title": "Se requiere autenticación",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Todavía puedes registrate o iniciar sesión en nuestra página o mediante google sign in.",
            "link": "auth.login"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(403)
    def page_restricted(e):
        e = {
            "title": "Página restringida",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Necesita permisos para entrar a esta página, no te sientas mal, mirar estos carros te hará sentir mejor.",
            "link": "home.home_page"
        }
        return render_template('errors.html' , e=e)

    @app.errorhandler(404)
    def page_not_found(e):
        e = {
            "title": PAGE_NOT_FOUND_TITLE,
            "code": e.code,
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(412)
    def invalid_request(e):
        e = {
            "title": "Solicitud inválida",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Alguno de los campos son inválidos, por favor, intente nuevamente.",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(500)
    def internal_server_error(e):
        e = {
            "title": PAGE_NOT_FOUND_TITLE,
            "code": "404",
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        e = {
            "title": PAGE_NOT_FOUND_TITLE,
            "code": "404",
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)