from flask import render_template
from werkzeug.exceptions import HTTPException


def error_handlers(app):

    @app.errorhandler(400)
    def bad_request(e):
        e = {
            "title": "Solicitud incorrecta",
            "code": e.code,
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Algo salio mal, falta algún parámetro o alguno no existe, intente nuevamente.",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(401)
    def auth_required(e):
        e = {
            "title": "Se requiere autenticación",
            "code": e.code,
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Todavía puedes registrate o iniciar sesión en nuestra página o mediante google sign in.",
            "link": "auth.login"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(403)
    def page_restricted(e):
        e = {
            "title": "Página restringida",
            "code": e.code,
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Necesita permisos para entrar a esta página, no te sientas mal, mirar estos carros te hará sentir mejor.",
            "link": "home.home_page"
        }
        return render_template('errors.html' , e=e)

    @app.errorhandler(404)
    def page_not_found(e):
        e = {
            "title": "Página no encontrada",
            "code": e.code,
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Parece que esta página que estás buscando, no existe. No te preocupes, todavía puedes encontrar tu carro de ensueño!",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(412)
    def invalid_request(e):
        e = {
            "title": "Solicitud inválida",
            "code": e.code,
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Alguno de los campos son invalidos, por favor, intente nuevamente.",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    @app.errorhandler(500)
    def internal_server_error(e):
        e = {
            "title": "Página no encontrada",
            "code": "404",
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Parece que esta página que estás buscando, no existe. No te preocupes, todavía puedes encontrar tu carro de ensueño!",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)

    
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        e = {
            "title": "Página no encontrada",
            "code": "404",
            "image": "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png",
            "description": "Parece que esta página que estás buscando, no existe. No te preocupes, todavía puedes encontrar tu carro de ensueño!",
            "link": "home.home_page"
        }
        return render_template('errors.html', e=e)