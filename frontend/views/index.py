from flask import Blueprint, render_template

from frontend.client.measurements import client

view = Blueprint('index', __name__)


@view.route('/')
def index():
    measurements = client.get_all()

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in measurements],
    )
