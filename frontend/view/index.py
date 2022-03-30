from flask import Blueprint, render_template

from frontend import measurements_client

view = Blueprint('index', __name__)


@view.route('/')
def index():
    all_measurements = measurements_client.get_all()

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in all_measurements],
    )
