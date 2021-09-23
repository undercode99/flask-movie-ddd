from .v1 import api_v1
def register_api(app):
    app.register_blueprint(api_v1, url_prefix="/api/v1")
