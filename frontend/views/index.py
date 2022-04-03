import httpx
from flask import Blueprint, flash, render_template, redirect, request, url_for

from frontend.config import config
from frontend.client.measurements import client

view = Blueprint('index', __name__)


@view.route('/')
def index():
    measurements = client.get_all()

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in measurements],
    )


@view.post('/upload')
def upload():
    if request.files:
        file = request.files['file']
        files = {'file': ('report.pdf', file)}
        timeout = httpx.Timeout(5.0, connect=5.0, read=50.0, write=5.0)
        r = httpx.post("http://185.252.146.250:5000/api/v1/upload/", files=files, timeout=timeout)
        if r.status_code != '201':
            flash(r.text)
            return redirect(url_for('index.index'))
        return redirect(url_for('index.index'))
    flash('No file')
    return redirect(url_for('index.index'))
