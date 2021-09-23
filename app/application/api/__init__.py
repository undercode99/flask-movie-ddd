from .v1 import api_v1
from app.application.http.response import Response

def register_api(app):
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    @app.errorhandler(404)
    def page_not_found(e):
        return Response().notfound()

