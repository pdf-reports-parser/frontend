from flask import Blueprint, render_template, redirect, url_for

from frontend.client.measurements import client
from frontend.forms.upload import FileForm

view = Blueprint('index', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    measurements = client.get_all()
    form = FileForm(meta={'csrf': False})

    if form.validate_on_submit():
        form.upload_file()
        return redirect(url_for('index.index'))

    return render_template(
        'index.html',
        measurements=[measurement.dict() for measurement in measurements],
        form=form,
    )
