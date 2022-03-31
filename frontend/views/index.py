from flask import Blueprint, render_template

from frontend.client.measurements import MeasurementsClient

view = Blueprint('index', __name__)
measurements_client = MeasurementsClient()


@view.route('/')
def index():
    all_measurements = measurements_client.get_all()

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in all_measurements],
    )
