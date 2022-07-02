from flask import jsonify
from werkzeug.exceptions import HTTPException

IMAGE_URL = "https://dbdzm869oupei.cloudfront.net/img/sticker/preview/19890.png"
GENERIC_DESCRIPTION = "Parece que la página que estás buscando no existe. No te preocupes, todavía puedes " \
                      "encontrar tu carro de ensueño! "
PAGE_NOT_FOUND_TITLE = "Página no encontrada"

LOGIN_PATH = "/login"
HOME_PATH = "/"


def error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        print(e)
        return jsonify({
            "title": "Peticion inválida",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "La petición que estás intentando hacer no es válida. Por favor, inténtalo de nuevo.",
            "redirect": LOGIN_PATH
        }), e.code

    @app.errorhandler(401)
    def auth_required(e):
        return jsonify({
            "title": "Se requiere autenticación",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Todavía puedes registrate o iniciar sesión en nuestra página o mediante google sign in.",
            "redirect": LOGIN_PATH
        }), e.code

    @app.errorhandler(403)
    def page_restricted(e):
        return jsonify({
            "title": "Página restringida",
            "code": e.code,
            "image": IMAGE_URL,
            "description": "Necesita permisos para entrar a esta página, no te sientas mal, mirar estos carros te hará sentir mejor.",
            "redirect": HOME_PATH
        }), e.code

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "title": PAGE_NOT_FOUND_TITLE,
            "code": e.code,
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "redirect": HOME_PATH
        }), e.code

    @app.errorhandler(412)
    def invalid_request(e):
        return jsonify({
            "title": PAGE_NOT_FOUND_TITLE,
            "code": e.code,
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "redirect": HOME_PATH
        }), e.code

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({
            "title": PAGE_NOT_FOUND_TITLE,
            "code": "404",
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "redirect": HOME_PATH
        }), 404

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        return jsonify({
            "title": PAGE_NOT_FOUND_TITLE,
            "code": "404",
            "image": IMAGE_URL,
            "description": GENERIC_DESCRIPTION,
            "redirect": HOME_PATH
        }), 404
