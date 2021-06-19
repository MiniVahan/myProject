# core/views.py
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get("page", 1, type=int)
    return render_template('index.html', page=page)


@core.route('/info')
def info():
    return render_template('info.html')
