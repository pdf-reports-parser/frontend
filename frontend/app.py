from flask import Flask

from frontend.config import config
from frontend.views import index
from frontend.views import measurement


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config.secret_key

    app.register_blueprint(index.view)
    app.register_blueprint(measurement.view, url_prefix='/measurements')

    return app
