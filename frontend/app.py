from flask import Flask

from frontend.views import index
from frontend.views import measurement


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(index.view)
    app.register_blueprint(measurement.view, url_prefix='/measurements')

    return app
