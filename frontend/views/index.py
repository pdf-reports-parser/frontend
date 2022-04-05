import httpx
from flask import Blueprint, flash, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename

from frontend.config import config
from frontend.client.measurements import client

view = Blueprint('index', __name__)
backend_url = config.backend_url
upload_url = f'{backend_url}/upload/'


class FileForm(FlaskForm):
    file = FileField()


@view.route('/', methods=['GET', 'POST'])
def index():
    measurements = client.get_all()
    form = FileForm(meta={'csrf': False})
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        files = {'file': (filename, file)}
        timeout = httpx.Timeout(5.0, connect=5.0, read=50.0, write=5.0)
        r = httpx.post(upload_url, files=files, timeout=timeout)
        if r.status_code != '201':
            flash(r.text)
            return redirect(url_for('index.index'))
        flash('got done')
        return redirect(url_for('index.index'))
    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in measurements],
        form=form,
    )
