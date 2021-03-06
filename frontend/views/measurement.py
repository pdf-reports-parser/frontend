from operator import itemgetter
from flask import Blueprint, render_template

from frontend.client.api import client

view = Blueprint('measurements', __name__)


@view.route('/<uid>')
def measurements(uid):
    measurement = client.measurements.get_by_id(uid)
    trials = client.trials.get_for_measurement(uid)
    title = f'Measurement {uid}'
    return render_template(
        'measurements.html',
        page_title=title,
        measurement=measurement.dict(),
        trials=sorted([trial.dict() for trial in trials], key=itemgetter('name')),
    )
