from flask import Blueprint, render_template

from frontend.client.measurements import client

view = Blueprint('measurements', __name__)


@view.route('/<uid>')
def measurements(uid):
    measurement = client.get_by_id(uid)
    return render_template('measurements.html', measurement=measurement.dict())
