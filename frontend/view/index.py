from flask import Blueprint, render_template

from frontend.client.measurements import MeasurementsClient

view = Blueprint('index', __name__)


@view.route('/')
def index():
    return render_template('index.html')
