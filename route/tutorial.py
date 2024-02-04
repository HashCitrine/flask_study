import os

from flask import Blueprint, Response, send_from_directory

bp = Blueprint('tutorial', __name__)


@bp.route('/', methods=['GET'])
def hello_world() -> Response:
    return Response('Hello world', 200)


@bp.route('/error', methods=['GET'])
def error():
    raise Exception('test error')


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
