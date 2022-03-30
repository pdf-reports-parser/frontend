from flask import Blueprint, render_template

from frontend import config, measurements_client

view = Blueprint('index', __name__)
app_config = config.load_from_env()


@view.route('/')
def index():
    all_measurements = measurements_client.get_all()

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in all_measurements],
    )
