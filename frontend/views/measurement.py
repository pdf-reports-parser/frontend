from flask import Blueprint, render_template

from frontend.client.measurements import MeasurementsClient

view = Blueprint('measurements', __name__)
measurements_client = MeasurementsClient()


@view.route('/<uid>')
def measurements(uid):
    measurement = measurements_client.get_by_id(uid)
    return render_template('measurements.html', measurement=measurement.dict())
